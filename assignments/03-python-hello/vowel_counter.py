#!/usr/bin/env python3
"""
Author : pmoma
Date   : 2019-02-05
Purpose: Count good
"""

import os
import sys

# --------------------------------------------------
def main():
    if len(sys.argv) != 2:
        print('Usage: {} WORD'.format(os.path.basename(sys.argv[0])))
        sys.exit(1)
    word=str(sys.argv[1])
    vowels=0
    for i in word:
        if (i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U'):
            vowels=vowels+1

    if vowels != 1:
        print('There are {} vowels in "{}."'.format(vowels, word))
    if vowels == 1:
        print('There is 1 vowel in "{}."'.format(word))

main()
