#!/usr/bin/env bash

set -u
DIR=${1:-$PWD/../../data/gapminder}

if [[ ! -d "$DIR" ]]; then
echo "$DIR is not a directory"
exit 1
fi

FILES=$(mktemp)
find "$DIR" -type f -name \* > "$FILES"
SORTED_FILES=$(mktemp)
sort -f "$FILES" > "$SORTED_FILES"
NUM_SORTED=$(wc $SORTED_FILES | awk '{print $DIR}')

echo $NUM_SORTED

if [[ $NUM_SORTED -lt 1 ]]; then
echo "No usable files in $DIR"
exit 1
fi

Trim1=$(basename .cc.txt $SORTED_FILES)

echo "$Trim1"

