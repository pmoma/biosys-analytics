#!/usr/bin/env python3
"""
Author : pmoma
Date   : 2019-02-12
Purpose: Cat-nate
"""

import os
import sys

# --------------------------------------------------
def main():
    args = sys.argv[1:]

    if len(args) != 1:
        print('Usage: {} FILE'.format(os.path.basename(sys.argv[0])))
        sys.exit(1)
        
    file = sys.argv[1]    
    if os.path.isfile(file) == False:
        print('{} is not a file'.format(file))
        sys.exit(1)
    
    with open(file) as i:
        for num, line in enumerate(i, start=1):
            print(' {}: {}'.format(num, line), end='') 
             
# --------------------------------------------------
main()
