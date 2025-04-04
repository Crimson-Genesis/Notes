#!/bin/bash
main=$1
shift
for word in $(tr ' ' '\n' < "$main" | sort | uniq); do
  count=0
  for file in "$@"; do
    wc=$(grep -o "\b$word\b" "$file" | wc -l)
    count=$((count + wc))
  done
  echo "$word: $count"
done
