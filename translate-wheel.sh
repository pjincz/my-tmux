#!/bin/bash

dir=$1

if [[ "$dir" == "up" ]]; then
  chr=A
elif [[ "$dir" == "down" ]]; then
  chr=B
else
  echo "bad dir: ${dir}" >&2
  exit 1
fi

read -a flags <<< "$(tmux display -p "#{pane_in_mode} #{mouse_any_flag} #{keypad_flag} #{alternate_on}")"

if [[ "${flags[0]}" == "1" ]]; then
  exit 1 # return 1 to indicate forward mouse message
else
  # normal mode
  if [[ "${flags[1]}" == "1" ]]; then
    # mouse support turned on, forward mouse message
    exit 1
  elif [[ "${flags[2]}" == "1" ]]; then
    # pad mode turn on, translate message to pad message
    tmux send-keys "^[" "O${chr}" "^[" "O${chr}" "^[" "O${chr}"
  elif [[ "${flags[3]}" == "1" ]]; then
    # smcup turned on, translate message to keyboard message
    tmux send-keys "^[" "[${chr}" "^[" "[${chr}" "^[" "[${chr}"
  else
    # normal shell case, turn copy-mode on
    tmux copy-mode -e
    exit 1
  fi
fi

