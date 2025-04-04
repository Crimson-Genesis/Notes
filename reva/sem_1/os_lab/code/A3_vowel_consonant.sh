#!/bin/bash
read -p "Enter a string: " str
v=0
c=0
for (( i=0; i<${#str}; i++ )); do
  ch="${str:$i:1}"
  case "$ch" in
    [aeiouAEIOU]) ((v++)) ;;
    [a-zA-Z]) ((c++)) ;;
  esac
done
echo "Vowels: $v, Consonants: $c"
