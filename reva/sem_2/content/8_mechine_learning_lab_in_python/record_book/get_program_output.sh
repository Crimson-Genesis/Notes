#!/usr/bin/env bash

output="prog_out.md"

for file in *.py; do
    echo "# $file\n===================" >> $output
    echo " " >> $output
    echo "## Code:- " >> $output
    echo "\`\`\`python" >> $output
    cat "$file" >> $output
    echo "\`\`\`" >> $output
    echo " " >> $output
    echo "## Output:- " >> $output
    echo "\`\`\`python" >> $output
    python "$file" >> $output
    echo "\`\`\`" >> $output
    echo "$file Done..."
done
