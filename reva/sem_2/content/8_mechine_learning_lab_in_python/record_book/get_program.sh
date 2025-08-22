#!/usr/bin/env bash

for file in *.py; do
    echo "# $file\n===================" >> program.md
    echo " " >> program.md
    echo "\`\`\`python" >> program.md
    cat "$file" >> program.md
    echo "\`\`\`" >> program.md
    echo "$file Done..."
done
