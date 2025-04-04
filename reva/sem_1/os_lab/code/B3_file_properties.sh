#!/bin/bash
read -p "Enter file name: " f
[[ -e "$f" ]] && ls -l "$f" || echo "File does not exist"
