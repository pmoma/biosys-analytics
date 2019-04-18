#!/usr/bin/env python3
"""
Author : pmoma
Date   : 2019-04-18
Purpose: K-mers
"""

import argparse
import sys
import os

from Bio import SeqIO

# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='K-mer Python script',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        'fasta', metavar='str', help='FASTA file')

    parser.add_argument(
        '-k',
	'--overlap',
        help='A named string argument',
        metavar='int',
        type=int,
        default=3)

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
def find_kmers(in_fasta, k):
    """function to find k mers of given length from string"""
    n= len(in_fasta)-k+1
    kmers=[]
    for i in range(0, n):
        kmers.append(in_fasta[i:i+k])
    return(kmers)

# --------------------------------------------------
def main():
    """Make a jazz noise here"""
    args = get_args()
    fasta = args.fasta
    kmer= args.overlap

    if kmer <= 1:
        die('-k "{}" must be a positive integer'.format(kmer))

    if not os.path.isfile(fasta):
        die('"{}" is not a file'.format(fasta))

    kstart={}
    kend={}
    with open(fasta, 'r') as f:
        for record in SeqIO.parse(f, "fasta"):
            kstart[record.id]=(find_kmers(record.seq, kmer)[0])
            kend[record.id]=(find_kmers(record.seq, kmer)[-1])
            
    for endk, endv in kend.items():
        for startk, startv in kstart.items():
            if endv in startv:
                if endk is not startk:
                    print(endk, startk)


# --------------------------------------------------
if __name__ == '__main__':
    main()

