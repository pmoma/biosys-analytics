#!/usr/bin/env python3
"""
Author : pmoma
Date   : 2019-02-22
Purpose: Rock the Casbah
"""

import argparse
import sys


# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='A Dynamite Python script',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        'word', metavar='Word', help='Your word to be \'sploded',nargs=1)

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
    word = args.word

    wordstr=word[0]
    for i,j in enumerate(wordstr, start=1):
        #print(i, j)
        print(wordstr[:i], end='')
    print()

# --------------------------------------------------
if __name__ == '__main__':
    main()

