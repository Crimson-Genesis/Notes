#!/bin/bash
for file in "$@"; do
  if [[ -f $file ]]; then
    tr 'a-z' 'A-Z' < "$file"
  else
    echo "$file not found"
  fi
done
