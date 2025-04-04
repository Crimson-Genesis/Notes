#!/bin/bash
for (( i=$#; i>0; i-- )); do
  echo "${!i}"
done
