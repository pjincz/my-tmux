#!/bin/bash

set -x

function list_pane() {
  tmux list-pane -F "#{pane_id} #{pane_top} #{pane_left} #{pane_active}"
}

function active_pane_id() {
  list_pane | grep "1$" | awk '{print $1}'
}

function top_pane_of() {
  cont=`list_pane`
  left=`echo "$cont" | grep "^$1 " | awk '{print $3}'`
  echo "$cont" | awk "\$3==$left{print}" | sort -k 2 -n | head -1 | awk '{print $1}'
}

function bottom_pane_of() {
  cont=`list_pane`
  left=`echo "$cont" | grep "^$1 " | awk '{print $3}'`
  echo "$cont" | awk "\$3==$left{print}" | sort -k 2 -n -r | head -1 | awk '{print $1}'
}

cur_pane_id=`active_pane_id`
top_pane_id=`top_pane_of ${cur_pane_id}`

declare -a breaked_pane=()

while true; do
  id=`bottom_pane_of ${top_pane_id}`
  if [[ "$id" == "${top_pane_id}" ]]; then
    break
  fi
  height=`tmux display -p -t $id "#{pane_height}"`
  breaked_pane+=($id:$height)
  tmux break-pane -d -s {bottom}
done

tmux split-window -h
new_pane_id=`active_pane_id`

last_id=$top_pane_id
for ((i=${#breaked_pane[@]}-1; i >= 0; --i)); do
  l=${breaked_pane[$i]}
  id=${l%:*}
  h=${l#*:}
  tmux join-pane -l $h -s $id -t $last_id
  last_id=$id
done

tmux select-pane -t $new_pane_id
