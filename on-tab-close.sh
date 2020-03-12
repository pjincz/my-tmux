#!/bin/bash

if [[ "$(tmux list-window | grep "" -c)" == "1" ]]; then
  sname=`tmux display -p "#{session_name}"`
  pid="%${sname%-*}"

  tmux swap-pane -d -t "$pid"
  tmux kill-session -t "$sname"
fi
