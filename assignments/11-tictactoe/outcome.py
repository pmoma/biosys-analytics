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
        description='Tic-Tac-Toe board',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        'state',
        help='Board state',
        metavar='state',
        type=str,
        default='.........')

    parser.add_argument(
        '-p', '--player', help='Player', metavar='str', type=str, default=None)

    parser.add_argument(
        '-c',
        '--cell',
        help='Cell to apply -p',
        metavar='int',
        type=int,
        default=None)

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
    state = args.state
    player = args.player
    cell = args.cell

    if player and player not in 'XO':
        die('Invalid player "{}", must be X or O'.format(player))

    if cell is not None and not 1 <= cell <= 9:
        die('Invalid cell "{}", must be 1-9'.format(cell))

    if any([player, cell]) and not all([player, cell]):
        die('Must provide both --player and --cell')

    if not re.search('^[.XO]{9}$', state):
        die('State "{}" must be 9 characters of only ., X, O'.format(state))

    cells = []

    for i, char in enumerate(state, start=1):
        cells.append(str(i) if char == '.' else char)

    winp = [[0,1,2],[3,4,5],[6,7,8],[0,4,8],[2,4,6],[0,3,6],[1,4,7],[2,5,8]]#three across three down both diagonals

    for player in ['X','O']:
        for i in winp:
            if all([cells[cell] == player for cell in i]):
                print('{} has won'.format(player))
                sys.exit()
    print('No winner')

# --------------------------------------------------

if __name__ == '__main__':

    main()

