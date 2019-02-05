#!/usr/bin/env python3
"""
Author : pmoma
Date   : 2019-02-05
Purpose: Be nice
"""

import os
import sys

# --------------------------------------------------
def main():
    names = sys.argv[1:]

    if len(names) == 0:
        print('Usage: {} NAME [NAME...]'.format(os.path.basename(sys.argv[0])))
        sys.exit(1)
    if len(names) == 1: 
        print('Hello to the 1 of you: ' + names[0] + '!')
    if len(names) == 2:
        print('Hello to the 2 of you: {}!'.format(' and '.join(names)))
    if len(names) > 2:
        print('Hello to the {} of you: {}, and {}!'.format(len(sys.argv[1:]), ', '.join(names[:-1]), ''.join(names[-1:])))
    else: sys.exit(1)

# --------------------------------------------------
main()
