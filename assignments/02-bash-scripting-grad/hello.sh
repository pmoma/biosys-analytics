#!/usr/bin/env bash

GREETING=$1
NAME=$2

if [[ $# -lt 1 ]] || [[ $# -gt 2 ]]; then
echo "Usage: hello.sh GREETING [NAME]"
exit 1
fi

if [[ $# -eq 1,2 ]]; then
echo "$GREETING, $NAME!" 
else
echo "$GREETING, Human!"
fi
