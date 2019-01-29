#! /bin/bash
#Peter Moma cat-n shell	script homework

i=0
FILE=$1

if [[ $# -lt 1 ]]; then
echo "Usage: cat-n.sh FILE"
exit 1
fi

if [[ ! -f "$FILE" ]]; then
echo "$FILE is not a file"
exit 2
fi

while read -r LINE; do
 i=$((i+1))
 echo "$i $LINE"
 done < "$FILE"
