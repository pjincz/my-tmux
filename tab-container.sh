#!/bin/bash

unset TMUX

pid=$1
tmux attach -t "${pid#%}-tabs"
