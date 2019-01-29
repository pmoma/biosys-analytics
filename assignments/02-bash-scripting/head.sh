#! /bin/bash
#Peter Moma head shell script homework

i=0
FILE=$1
OPTIONAL_ARG=$2

if [[ $# -eq 0 ]]; then
echo "Usage: head.sh FILE OPTIONAL_ARG"
exit 1
fi

if [[ ! -f "$FILE" ]]; then
echo "$FILE is not a file"
exit 2
fi

while read -r LINE; do
i=$((i+1))
echo "$i $LINE"

if [[ $# -gt 1 ]] && [[ $i -eq OPTIONAL_ARG ]]; then
break
fi

if [[ $# -lt 2 ]] && [[ $i -eq 3 ]]; then
break
fi

done < "$FILE"
