#!/usr/bin/env python3
"""
Author : pmoma
Date   : 2019-02-14
Purpose: Winning doubloons
"""

import os
import argparse
import sys

# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Play a game of tic-tac-toe',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
        
    parser.add_argument(
        '-c',
	'--cell',
        help='Pick a cell (1-9)',
        metavar='int',
        type=int,
        choices=[1,2,3,4,5,6,7,8,9],
        dest='cell')

    parser.add_argument(
        '-p',
	'--player',
        help='Player Team: X or O',
        metavar='str',
        type=str,
        choices=['X','O'],
        dest='player')
        
    parser.add_argument(
        '-s',
	'--state',
        help='Set a game state',
        metavar='str',
        type=str,
        default='.........',
        choices=['X','O','.'],
        dest='state')
        #action="store_true")    

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
    args = get_args()
    state = args.state
    cell = args.cell
    player = args.player
    print(state)
    
# --------------------------------------------------
if __name__ == '__main__':
    main()
