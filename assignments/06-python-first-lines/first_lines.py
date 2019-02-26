#!/usr/bin/env python3
"""
Author : pmoma
Date   : 2019-02-22
Purpose: Make a poetry anthology
"""

from __future__ import print_function
import argparse
import sys
import os

# --------------------------------------------------
def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)


# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Argparse Python script',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        'positional', metavar='DIR', nargs='+', help='DIR')

    parser.add_argument(
        '-w',
	'--width',
        metavar='int',
        type=int,
        default=50)

    return parser.parse_args()

# --------------------------------------------------
def warn(msg):
    """Print a message to STDERR"""
    print(msg, file=sys.stderr)


# --------------------------------------------------
def die(msg='Something bad happened'):
    """warn() and exit with error"""
    warn(msg)
    sys.exit(1)


# --------------------------------------------------
def main():
    """Make a jazz noise here"""
    args = get_args()
    dir = args.positional
    lwidth = args.width

#    print('line width = "{}"'.format(lwidth))
#    print('poetry directory = "{}"'.format(dir))
    
    for i in dir:
        if os.path.isdir(i) == False:
            eprint('"{}" is not a directory'.format(i))
            dir.remove(i)
            continue
    
#    print('{}'.format(dir))
    
    for i in dir:
        for filename in os.listdir(i):
            print(filename)
            with open(filename) as f:
                for line in f:
                    print(line)
                    break       
            
            
            

    
    
    
    
    
    
    


# --------------------------------------------------
if __name__ == '__main__':
    main()
