#!/bin/bash

repeat=`tmux display -p "#{@repeat}"`
if [[ "${repeat}" -gt 0 ]]; then
  if [[ "${repeat}" -gt 10000 ]]; then
    tmux display "Can only repeat 10000 times at most"
    exit 0
  fi
  tmux send -N "$repeat"
  tmux set @repeat ""
fi
