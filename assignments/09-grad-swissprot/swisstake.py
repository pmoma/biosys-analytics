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
    out=open(outf,'wt')
    with open(file) as fil:
        for record in SeqIO.parse(fil, 'swiss'):
#            print(record.annotations)
#            pp.pprint(record.annotations)
            words=record.annotations.get('keywords', None)
            taxa=record.annotations.get('taxonomy', None)
            if words:
#                print(words)
                for j, k in itertools.product(skip, taxa):
                    print(k.casefold(), j.casefold())
                    if k.casefold() == j.casefold():
                        numb+=1
                        break
                for i in words:
#                    print(i)
                    if i.casefold() == kword.casefold():
#                        print('match', i, kword)
                         SeqIO.write(record, out, 'fasta')
                         numg+=1
            else:
                die('Bad file, no keyword term.')
    out.close()
    
    print('Done, skipped {} and took {}. See output in "{}".'.format(numb,numg,outf))

# --------------------------------------------------
if __name__ == '__main__':
    main()
