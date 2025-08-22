#!/usr/bin/env bash

for file in *.py; do
    echo "$file\n===================" >> output.md
    echo " " >> output.md
    echo "\`\`\`python" >> output.md
    python "$file" >> output.md
    echo "\`\`\`" >> output.md
    echo "$file Done..."
done
