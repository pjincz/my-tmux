#!/bin/bash

SEL=clip

IFS=
xclip -o -sel "$SEL" | while read -r -d '' -n 1 ch; do
  echo -n "$ch"
  sleep 0.02
done
