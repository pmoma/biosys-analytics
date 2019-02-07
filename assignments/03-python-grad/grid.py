#!/usr/bin/env python3
"""
Author : pmoma
Date   : 2019-02-07
Purpose: Enter the Matrix
"""

import os
import sys

# --------------------------------------------------
def main():
    inputnum = sys.argv[1:]
    if len(inputnum) != 1:
        print('Usage: {} NUM'.format(os.path.basename(sys.argv[0])))
        sys.exit(1)

    number = int(sys.argv[1])
    
    if number not in range(2,10):
        print('NUM ({}) must be between 1 and 9'.format(number))
        sys.exit(1)
    posnum=[2,3,4,5,6,7,8,9]
    if number in range(2,10):
        for count, i in enumerate(range(1,number**2 +1)):
            print('{0:3}'.format(i), end='')
            if (count+1)%number == 0:
                print('')
                

# --------------------------------------------------
main()
