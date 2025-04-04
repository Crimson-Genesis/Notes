#!/bin/bash
read -p "Enter numbers: " -a arr
max=${arr[0]}
min=${arr[0]}
for n in "${arr[@]}"; do
  (( n > max )) && max=$n
  (( n < min )) && min=$n
done
echo "Max: $max, Min: $min"
