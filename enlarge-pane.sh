#!/bin/bash

h=`tmux display -p "#{pane_height}"`
adj=$1

if [[ -a "$adg" ]]; then
  adj=1
fi

r=$((h+adj))
if [[ "$r" -lt 1 ]]; then
  r=1
fi

tmux resize-pane -y "$r"
