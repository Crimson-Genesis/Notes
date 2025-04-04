#!/bin/bash
day=$(date +%-d)
cal | sed "s/\b$day\b/${#day}==1 && echo '*'$day || echo '**'$day/'/e"
