#!/bin/bash
read -p "Enter m: " m
read -p "Enter n: " n
for (( i=m; i<=n; i++ )); do
  prime=1
  for (( j=2; j*j<=i; j++ )); do
    if (( i % j == 0 )); then prime=0; break; fi
  done
  (( i > 1 && prime )) && echo "$i"
done
