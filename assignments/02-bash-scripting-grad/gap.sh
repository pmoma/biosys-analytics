#!/usr/bin/env bash

set -u
DIR=${1:-$PWD/../../data/gapminder}

if [[ ! -d "$DIR" ]]; then
echo "$DIR is not a directory"
exit 1
fi

FILES=$(mktemp)
find "$DIR" -type f -name \*.cc.txt > "$FILES"
SORTED_FILES=$(sort -i "$FILES" | awk'{print $1}')

if [[ $SORTED_FILES -lt 1 ]]; then
echo "No usable files in $DIR"
exit 1
fi

i=0
while read -r FILENAME; do
BASENAME=$(basename "$FILENAME")
printf "%3d: %s\n" $i "$FILENAME"
done < "$FILES"

echo "$i $BASENAME"
