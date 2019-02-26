#!/usr/bin/env python3
"""
Author : pmoma
Date   : 2019-02-22
Purpose: Make a poetry anthology
"""

import argparse
import sys
import os

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
    dirs = args.positional
    lwidth = args.width

#    print('line width = "{}"'.format(lwidth))
#    print('poetry directory = "{}"'.format(dir))
#    print('{}'.format(dir))
    
    for d in dirs:
        if not os.path.isdir(d):
            warn('"{}" is not a directory'.format(d))
            continue
        for filename in os.listdir(d):
            print(filename)
            with open(filename) as fh:
                for line in f:
                    print(line)
                    break       
            
            
    
    
    


# --------------------------------------------------
if __name__ == '__main__':
    main()
