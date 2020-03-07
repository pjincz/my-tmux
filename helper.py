#!/usr/bin/python3

import sys
import subprocess
from collections import namedtuple

BoxBase = namedtuple('BoxBase',
             ['type', 'w', 'h', 'x', 'y', 'children', 'pane_id'])

class Box(BoxBase):

  def find_pane(self, pane_id):
    if self.pane_id == pane_id:
      return self

    for box in self.children:
      r = box.find_pane(pane_id)
      if r:
        return r

    return None

def layout_checksum(x):
  csum = 0
  for ch in x:
    csum = (((csum >> 1) | (csum << 15)) + ord(ch)) & 0xffff
  return "%04x" % csum

class LayoutParser:

  def parse(self, cont):
    csum, layout = cont.split(',', 1)
    if layout_checksum(layout) != csum:
      raise Exception('checksum error')

    self._str = layout
    self._cur = 0

    return self.parse_boxes()[0]

  def parse_box(self):
    w = self.take_int()
    assert self.take_char() == 'x'
    h = self.take_int()
    assert self.take_char() == ','
    x = self.take_int()
    assert self.take_char() == ','
    y = self.take_int()

    ch = self.take_char()
    if ch == ',':
      pane_id = self.take_int()
      return Box('pane', w, h, x, y, [], '%' + str(pane_id))
    elif ch == '{':
      children = self.parse_boxes()
      assert self.take_char() == '}'
      return Box('hbox', w, h, x, y, children, None)
    elif ch == '[':
      children = self.parse_boxes()
      assert self.take_char() == ']'
      return Box('vbox', w, h, x, y, children, None)
    else:
      assert False
    
  def parse_boxes(self):
    boxes = []
    while True:
      boxes.append(self.parse_box())
      if self.peek_char() == ',':
        self.take_char()
      else:
        break
    return boxes

  def take_char(self):
    if self._cur < len(self._str):
      ch = self._str[self._cur]
      self._cur += 1
      return ch

    return ''

  def peek_char(self):
    return self._str[self._cur] if self._cur < len(self._str) else ''

  def take_int(self):
    x = 0
    while self.peek_char() >= '0' and self.peek_char() <= '9':
      x = x * 10 + int(self.take_char())
    return x


class Tmux:

  Window = namedtuple('Window', ['id', 'active', 'layout'])
  
  def run_command(self, *args):
    r = subprocess.run(['tmux'] + list(args),
                       capture_output=True, encoding='utf-8')
    return r.stdout

  def query(self, *fields):
    sep = '--5763599105--'
    query = sep.join('#{'+x+'}' for x in fields)
    line = self.run_command('display', '-p', '-F', query).strip()
    return namedtuple('info', fields, rename=True)(*line.split(sep))

  def setw(self, key, value):
    self.run_command('setw', key, str(value))

  def select_pane(self, pane_id):
    self.run_command('select-pane', '-t', pane_id)


def select_column(idx_1base):
  idx = idx_1base - 1
  tmux = Tmux()
  info = tmux.query('window_layout', 'pane_id')
  layout = LayoutParser().parse(info[0])
  current_pane = info.pane_id

  if layout.type != 'hbox':
    tmux.display('Not in column-based layout')
    return False

  columns = layout.children
  if idx < 0 or idx >= len(columns):
    tmux.display('Column ' + idx_1base + ' does not exists')
    return False

  for i in range(len(columns)):
    if columns[i].find_pane(current_pane):
      current_column = i
      break

  if idx == current_column:
    return False

  info = tmux.query('@column_' + str(idx) + '_last_pane')

  if columns[idx].find_pane(info[0]):
    raise_pane = info[0]

  else:
    box = columns[idx]
    while box.type != 'pane':
      box = box.children[0]

    raise_pane = box.pane_id

  tmux.setw('@column_' + str(current_column) + '_last_pane', current_pane)
  tmux.select_pane(raise_pane)


def test():
  tmux = Tmux()
  tmux.run_command('display', 'test')


def main(cmd, args):
  if cmd == 'test':
    test()

  elif cmd == 'select-column':
    assert len(args) == 1
    select_column(int(args[0]))

  else:
    raise Exception('unknown subcommand: ' + cmd)


if __name__ == '__main__':
  assert len(sys.argv) > 2
  main(sys.argv[1], sys.argv[2:])

