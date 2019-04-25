#!/usr/bin/env python3
"""
Author : pmoma
Date   : 2019-04-24
Purpose: Get freaky
"""
from collections import defaultdict
import argparse
import sys
import re

# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Argparse Python script',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        'file', metavar='file', nargs='+', help='The file you want to count from', type=argparse.FileType('r', encoding='UTF-8'))

    parser.add_argument(
        '-s',
	'--sort',
        help='Sort by word or frequency',
        metavar='str',
        type=str,
        default='word')

    parser.add_argument(
        '-m',
	'--min',
        help='Integer value indicating the minimum number of times a word must occur to be included in the output',
        metavar='int',
        type=int,
        default=0)

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
    file = args.file
    sortopt = args.sort
    min = args.min

    re.sub('[^a-zA-Z0-9]', '', 'f)0o_,b@a,>r!')


    wcount=defaultdict(int)
    for c in file:
        words= c.read().split()
        words= [re.sub('[^a-zA-Z0-9]', '', n).lower() for n in words]
        for i in words:
            wcount[i]+=1

    if sortopt== 'word':
        pairs= sorted([(word, count) for word, count in wcount.items()])
        for word, count in pairs:
            if count >= min and word is not '':
                print('{:20} {}'.format(word, count))
    elif sortopt== 'frequency':
        pairs= sorted([(count, word) for word, count in wcount.items()])
        for count, word in pairs:
            if count >= min and word is not '':
                print('{:20} {}'.format(word, count))
    else:
        die('unrecognized sorting option use \'word\' or \'frequency\'')
# --------------------------------------------------
if __name__ == '__main__':
    main()

