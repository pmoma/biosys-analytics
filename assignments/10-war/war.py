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
    b = list(map(str, range(2,11)))+list('JQKA')
    tdeck=(list(product(a, b)))
    deck=sorted(tdeck)
#    print(deck)
#    print(tdeck)  
    random.shuffle(deck)
  
    p1w=0
    p2w=0
    while len(deck)>0:
        card1=deck.pop()
        card2=deck.pop()
#        print(card1,card2)
#        print('test')

        if card1[1] == 'J':
            pcard1=('11')
        elif card1[1] == 'Q':
            pcard1=('12')
        elif card1[1] == 'K':
            pcard1=('13')
        elif card1[1] == 'A':
            pcard1=('14')
        else:
            pcard1=card1[1]
        
        if card2[1] == 'J':
            pcard2=('11')
        elif card2[1] == 'Q':
            pcard2=('12')
        elif card2[1] == 'K':
            pcard2=('13')
        elif card2[1] == 'A':
            pcard2=('14')
        else:
            pcard2=card2[1]
            
        cstr=('{:>3} {:>3}'.format(''.join(card1), ''.join(card2)))

        if int(pcard1)>int(pcard2):
            print(cstr,'P1')
            p1w+=1
        elif int(pcard1)<int(pcard2):
            print(cstr,'P2')
            p2w+=1
        else:
            print(cstr,'WAR!')
    if p1w>p2w:
        winner='Player 1'
    elif p1w<p2w:
        winner='Player 2'
    else:
        winner='DRAW'
    
    if winner != 'DRAW':
        print('P1 {} P2 {}: {} wins'.format(p1w,p2w,winner))
    else:
        print('P1 {} P2 {}: {}'.format(p1w,p2w,winner))    
        
        

# --------------------------------------------------
if __name__ == '__main__':
    main()

