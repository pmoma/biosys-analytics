#!/usr/bin/env bash

set -u
DIR=$PWD/../../data/gapminder

 function lc() {
wc -l "$1" | awk'{print $1}'
    }
    
function USAGE() {
printf "Usage:\n  %s -i DIR \n\n" "$(basename "$0")"
  echo "Required arguments:"
  echo " -i DIR"
  
  echo
exit "${1:-0}"
}

[[ $# -eq 0 ]] && USAGE 1

while getopts :i:h OPT; do
case $OPT in
h)
USAGE
;;
i)
DIR="$OPTARG"
;;
:)
echo "Error: Option -$OPTARG requires an argument."
exit 1
;;
\?)
echo "Error: Invalid option: -${OPTARG:-""}"
exit 1
esac
done

if [[ ! -d "$DIR" ]]; then
echo "$DIR is not a directory"
exit 1
fi

FILES_LIST=$(mktemp)
 i=0
 while read -r FILE; do
 BASENAME=$(basename "$FILE")
 let i++
 echo "$i $BASENAME"
 wc -l "$FILE" > "$OUT_DIR/$BASENAME"
 done < "$FILES_LIST"
 echo "$FILES_LIST"
rm "$FILES_LIST"
 
