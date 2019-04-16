#!/usr/bin/env python3
"""
Author : pmoma
Date   : 2019-04-16
Purpose: Hamm
"""
import logging
import argparse
import sys
import re
import os
# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Hamming Python script',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        'positionals', metavar='FILE', nargs=2, help='File inputs')

    parser.add_argument(
        '-d',
	'--debug',
        help='Debug',
        type=bool,
        default=False)

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
def dist(s1,s2):
    """Hamming code"""
    num= abs(len(s1)-len(s2))
    for l1, l2 in list(zip(s1,s2)):
        if l1!= l2:
            num+= 1

    logging.debug('s1 = {}, s2 = {}, d = {}'.format(s1,s2,num))
    return num

# --------------------------------------------------
def main():
    args = get_args()
    fil = args.positionals

    if len(fil) !=2:
        die('Only two files')
    if not os.path.isfile(fil[0]):
        die('"{}" is not a file'.format(fil[0]))
    if not os.path.isfile(fil[1]):
        die('"{}" is not a file'.format(fil[1]))
    logging.basicConfig(
    filename='.log',
    filemode='w',
    level=logging.DEBUG if args.debug else logging.CRITICAL
)
    logging.debug('file1 = {}, file2 = {}'.format(fil[0], fil[1]))

    dis = 0
    fil1= open(fil[0]).read().split()
    fil2= open(fil[1]).read().split()
    ftot= list(zip(fil1, fil2))
    #print(ftot)
    for s1, s2 in ftot:
        dis += dist(s1, s2)

    print(dis)
# --------------------------------------------------
if __name__ == '__main__':
    main()

