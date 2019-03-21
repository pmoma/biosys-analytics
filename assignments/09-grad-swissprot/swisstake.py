#!/usr/bin/env python3
"""
Author : pmoma
Date   : 2019-03-21
Purpose: Parse Swissprot
"""

from Bio import SeqIO
import argparse
import sys
import os
import csv
import pprint
import itertools


# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Filter Swissprot file for keywords, taxa',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        'file', metavar='FILE', help='Uniprot file')

    parser.add_argument(
        '-s',
	'--skip',
        help='Skip taxa',
        metavar='str',
        type=str,
        default='',
        nargs='+')

    parser.add_argument(
        '-k',
	'--keyword',
        help='Take on keyword',
        metavar='str',
        type=str,
        default=None,
        required=True)

    parser.add_argument(
        '-o',
	'--output',
        help='Output filename',
        metavar='FILE',
        type=str,
        default='out.fa')
        
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
    skip = args.skip
    kword = args.keyword
    outf = args.output
    pp = pprint.PrettyPrinter(indent=4)
    
    
    if not os.path.isfile(file):
        die('"{}" is not a file'.format(file))
    
    
    print('Processing "{}"'.format(file)) 
    
    numg=0
    numb=0
    with open(outf, 'w') as outfh:
        for record in SeqIO.parse(file, 'swiss'):
            annt=record.annotations
            if skip and 'taxonomy' in annt:
                taxa=set(map(str.lower,annt['taxonomy']))
                skipp=set(map(str.lower,skip))
                if skipp.intersection(taxa):
                    numb+=1
                    continue
            if 'keywords' in annt:
                kw=set(map(str.lower,annt['keywords']))
                if kword in kw:
                    numg+=1
                    SeqIO.write(record,outfh,'fasta')
                else:
                    numb+=1
    print('Done, skipped {} and took {}. See output in "{}".'.format(numb,numg,outf))

# --------------------------------------------------
if __name__ == '__main__':
    main()
