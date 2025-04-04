#!/bin/bash
read -p "Enter a string: " str
rev=$(echo "$str" | rev)
[[ "$str" == "$rev" ]] && echo "Palindrome" || echo "Not a palindrome"
