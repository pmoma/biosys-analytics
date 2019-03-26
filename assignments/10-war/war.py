#!/usr/bin/env python3
"""
Author : pmoma
Date   : 2019-02-22
Purpose: Rock the Casbah
"""

import argparse
import sys
import random
from itertools import product

# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='"War" cardgame',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        '-s',
	'--seed',
        help='Random seed',
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
    seed = args.seed

    if seed is not None:
        random.seed(seed)
        
    a = list('♥♠♣♦')
    b = range(2,15)
    deck=(sorted(product(a, b)))
#    print(deck)
    random.shuffle(deck)
#    print(deck)    
    p1w=0
    p2w=0
    while len(deck)>0:
        card1=deck.pop()
        card2=deck.pop()
#        print(card1,card2)
#        print('test')

        if card1[1] == 11:
            pcard1=('J')
        elif card1[1] == 12:
            pcard1=('Q')
        elif card1[1] == 13:
            pcard1=('K')
        elif card1[1] == 14:
            pcard1=('A')
        else:
            pcard1=card1[1]
        
        if card2[1] == 11:
            pcard2=('J')
        elif card2[1] == 12:
            pcard2=('Q')
        elif card2[1] == 13:
            pcard2=('K')
        elif card2[1] == 14:
            pcard2=('A')
        else:
            pcard2=card2[1]
        cstr=(' {}{}  {}{}'.format(card1[0], pcard1, card2[0], pcard2))
        if card1[1]>card2[1]:
            print(cstr,' P1')
            p1w+=1
        elif card1[1]<card2[1]:
            print(cstr,' P2')
            p2w+=1
        else:
            print(cstr,' War!')
    if p1w>p2w:
        winner='Player 1'
    elif p1w<p2w:
        winner='Player 2'
    else:
        winner='DRAW'
    print('P1 {} P2 {}: {} wins'.format(p1w,p2w,winner))
    
        
        

# --------------------------------------------------
if __name__ == '__main__':
    main()

