#!/bin/bash
sum=0
for n in "$@"; do
  sum=$((sum + n))
done
echo "Sum: $sum"
