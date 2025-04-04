#!/bin/bash
read -p "Enter numbers separated by space: " -a nums
sum=0
for i in "${nums[@]}"; do
  sum=$((sum + i))
done
echo "Sum: $sum"
