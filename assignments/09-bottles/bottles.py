#!/usr/bin/env python3
"""
Author : pmoma
Date   : 2019-03-19
Purpose: Have a few drinks
"""

import argparse
import sys

# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Bottles of beer song',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        '-n',
	'--num_bottles',
        help='A named integer argument',
        metavar='INT',
        type=int,
        default=10)

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
    nbot = args.num_bottles

    if nbot <= 0:
    	die('N {} must be a positive integer'.format(nbot))
    song="""{} bottles of beer on the wall,
{} bottles of beer,
Take one down, pass it around,
{} bottles of beer on the wall!"""
    song2="""{} bottles of beer on the wall,
{} bottles of beer,
Take one down, pass it around,
{} bottle of beer on the wall!"""
    song1="""{} bottle of beer on the wall,
{} bottle of beer,
Take one down, pass it around,
{} bottles of beer on the wall!"""
    
    c=0
    while c < nbot:
        cur=nbot-c
        if cur > 2:
            print(song.format(cur,cur,cur-1))
            print()
        elif cur == 2:
            print(song2.format(cur,cur,cur-1))
            print()
        else:
            print(song1.format(cur,cur,cur-1))
            
        c += 1    

# --------------------------------------------------
if __name__ == '__main__':
    main()

