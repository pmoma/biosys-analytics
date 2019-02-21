#!/usr/bin/env python3
"""
Author : pmoma
Date   : 2019-02-21
Purpose: Tic-Tac-Toe outcomes

"""

import argparse
import re
import os
import sys

# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Tic-Tac-Toe board outcomes',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        'positional',
        help='Board state',
        metavar='str',
        type=str,
        default='.........')

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
    state = args.positional

    if not re.search('^[.XO]{9}$', state):
        die('State "{}" must be 9 characters of only ., X, O'.format(state))

    wins = {'XXX......': 'X',
		'X..X..X..': 'X',
		'X...X...X': 'X',
		'.X..X..X.': 'X',
		'..X.X.X..': 'X',
		'..X..X..X': 'X',
		'...XXX...': 'X',
		'......XXX': 'X',
		'OOO......': 'O',
		'O..O..O..': 'O',
		'O...O...O': 'O',
		'.O..O..O.': 'O',
		'..O.O.O..': 'O',
		'..O..O..O': 'O',
		'...OOO...': 'O',
		'......OOO': 'O'}
    
    
#    for i in wins:
#        i[1],i[0]
#    print(state)
    if state in wins.keys():
        print('{} has won'.format(wins.get(state)))
    else:
        print('No winner')

# --------------------------------------------------

if __name__ == '__main__':

    main()
