#!/usr/bin/env python3
"""
Author : pmoma
Date   : 2019-02-19
Purpose: translation
"""

import argparse
import sys
import os

# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Argparse Python script',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        '-c',
	'--codons',
        help='A file with codon translations ',
        metavar='str',
        type=str,
        required=True)

    parser.add_argument(
        '-o',
	'--outfile',
        help='Output filename ',
        metavar='str',
        type=str,
        default='out.txt')

    parser.add_argument(
        'positional', metavar='str', help='DNA/RNA sequence')

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
    ctable = args.codons
    out = args.outfile
    sequence = args.positional

    if os.path.isfile(ctable) == False:
        print('--codons "{}" is not a file'.format(ctable))
        sys.exit(1)
    if os.path.isfile(out) == True:
        print('Outfile already exists, append sequence?')
        cont=input('(Yes) to append: ')
    else:
        cont='Yes'
    if cont != 'Yes':
        sys.exit(1)
    
    cdict = {}
    with open(ctable) as f:
        for line in f:
           (key, val) = line.split()
           cdict[key] = val
#    print(cdict)
#    print('ctable = "{}"'.format(ctable))
#    print('sequence = "{}"'.format(sequence))
    if os.path.isfile(sequence) == True:
    	with open(sequence, 'r') as seqfile:
            seq=seqfile.read().replace('\n', '').upper()
    else:
        seq=sequence.upper()
    
#    print('Seq = {}'.format(seq))
    
    seqcod= [seq[i:i+3] for i in range(0, len(seq), 3)]
#    print(seqcod)
#    print(cdict.keys())    
    for i,c in enumerate(seqcod):
        if c in cdict:
            print(cdict.get(c), end='', file=open(out, "a"))
        else:
            print('-', end='', file=open(out, "a"))
    
    print('Output written to "{}"'.format(out))

# --------------------------------------------------
if __name__ == '__main__':
    main()

