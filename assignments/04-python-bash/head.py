#!/usr/bin/env python3
"""
Author : pmoma
Date   : 2019-02-12
Purpose: Headbang
"""

import os
import sys

# --------------------------------------------------
def main():
    args = sys.argv[1:]

    if len(args) < 1:
        print('Usage: {} FILE NUMBER'.format(os.path.basename(sys.argv[0])))
        sys.exit(1)
        
    if len(args) > 2:
        print('Usage: {} FILE NUMBER'.format(os.path.basename(sys.argv[0])))
        sys.exit(1)
        
    file = sys.argv[1]    
    if os.path.isfile(file) == False:
        print('{} is not a file'.format(file))
        sys.exit(1)
        
    if len(args) == 2:
    	num = int(sys.argv[2])
    else:
        num = 3
    	
    if num < 1:
        print('lines ({}) must be a positive number'.format(num))
        sys.exit(1)        
    
    i = 0        
    while i > num:
        with open(file) as i:
            for line in i:
                print('{}'.format(line), end='')
                i += 1
    
# --------------------------------------------------
main()
