#!/usr/bin/env python3
"""
Author : pmoma
Date   : 2019-03-28
Purpose: Blackjack
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
    parser.add_argument(
        '-d',
	'--dealer_hits',
        help='extra card',
        action='store_true')
        
    parser.add_argument(
        '-p',
	'--player_hits',
        help='extra card',
        action='store_true')

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
    dealer_hits = args.dealer_hits
    player_hits = args.player_hits

    if seed is not None:
        random.seed(seed)
        
    a=list('♥♠♣♦')
    b=list(map(str, range(2,11)))+list('JQKA')
    tdeck=(list(product(a, b)))
    deck=sorted(tdeck)
#    print(tdeck)  
    random.shuffle(deck)
#    print(deck)
    cardn=dict([(str(i), int(i)) for i in range(2,11)])
    cardn.update({'J':10, 'Q':10, 'K':10, 'A':1})
#    print(cardn)
    dcards=[]
    pcards=[]
    
    for i in (1,2):
        pcards.append(deck.pop())
        dcards.append(deck.pop())
    if player_hits:
        pcards.append(deck.pop())
    if dealer_hits:
        dcards.append(deck.pop())
#    print(pcards)
 #   print(dcards)
    
    ptot=0    
    dtot=0
    pcardp=[]
    for i in pcards:
        pcardstr=i[0]+i[1]
        pcardp.append(pcardstr)
        ptot+=cardn[i[1]]
#    print(pcardp)
    dcardp=[]
    for j in dcards:
        dcardstr=j[0]+j[1]
        dcardp.append(dcardstr)
        dtot+=cardn[j[1]]
#    print(dcardp) 
    
    
    if player_hits and dealer_hits:
        print('''D [{:>2}]: {} {} {}
P [{:>2}]: {} {} {}'''.format(dtot,dcardp[0],dcardp[1], dcardp[2],ptot,pcardp[0],pcardp[1], pcardp[2]))
    elif player_hits:
        print('''D [{:>2}]: {} {}
P [{:>2}]: {} {} {}'''.format(dtot,dcardp[0],dcardp[1],ptot,pcardp[0],pcardp[1], pcardp[2]))        
    elif dealer_hits:
        print('''D [{:>2}]: {} {} {}
P [{:>2}]: {} {}'''.format(dtot,dcardp[0],dcardp[1], dcardp[2],ptot,pcardp[0],pcardp[1]))
    else:
        print('''D [{:>2}]: {} {}
P [{:>2}]: {} {}'''.format(dtot,dcardp[0],dcardp[1],ptot,pcardp[0],pcardp[1]))
    
    if ptot>21: 
        print("Player busts! You lose, loser!")
        exit(0)
    if dtot>21: 
        print("Dealer busts.")
        exit(0)
    if ptot==21: 
        print("Player wins. You probably cheated.")
        exit(0)
    if dtot==21: 
        print("Dealer wins!")
        exit(0)
    if dtot<18: 
        print("Dealer should hit.")
    if ptot<18: 
        print("Player should hit.")  
    
        

# --------------------------------------------------
if __name__ == '__main__':
    main()

