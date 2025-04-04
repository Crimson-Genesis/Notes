#!/bin/bash
read -p "Enter 3 numbers: " a b c
min=$a
(( b < min )) && min=$b
(( c < min )) && min=$c
echo "Smallest: $min"
