#!/bin/bash
file=$1
if [[ -e "$file" ]]; then
  stat "$file" | grep -i "Birth" || echo "Birth time not available"
else
  echo "File not found"
fi
