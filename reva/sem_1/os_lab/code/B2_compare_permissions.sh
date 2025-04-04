#!/bin/bash
perm1=$(stat -c %A "$1" 2>/dev/null)
perm2=$(stat -c %A "$2" 2>/dev/null)

if [[ "$perm1" == "$perm2" ]]; then
  echo "Common permissions: $perm1"
else
  echo "$1: $perm1"
  echo "$2: $perm2"
fi
