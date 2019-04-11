#!/usr/bin/env python3
"""
Author : pmoma
Date   : 2019-04-11
Purpose: CDHIT parse
"""

import argparse
import sys
import os
import re
from Bio import SeqIO

# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Argparse Python script',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        '-c',
	'--cdhit',
        help='Output file from CD-HIT (clustered proteins)',
        metavar='str',
        type=str,
        default=None,
        required=True)

    parser.add_argument(
        '-p',
	'--proteins',
        help='Proteins FASTA',
        metavar='str',
        type=str,
        default=None,
        required=True)

    parser.add_argument(
        '-o',
	'--outfile',
        help='Output file',
        metavar='str',
        type=str,
        default='unclustered.fa')

    return parser.parse_args()

# --------------------------------------------------
def warn(msg):
    """Print a message to STDERR"""
    print(msg, file=sys.stderr)

# --------------------------------------------------
def die(msg=' '):
    """warn() and exit with error"""
    warn(msg)
    sys.exit(1)

# --------------------------------------------------
def main():
    """Make a jazz noise here"""
    args = get_args()
    cdh = args.cdhit
    prot = args.proteins
    outf = args.outfile

    if not os.path.isfile(prot):
        die('--proteins "{}" is not a file'.format(prot))

    if not os.path.isfile(cdh):
        die('--cdhit "{}" is not a file'.format(cdh))

    cluster=set()
    with open(cdh, 'r') as cdhf:
        for line in cdhf:
            match=re.search(r'>gi\|(\d+)\|', line)
            if match:
                cluster.add(match.group(1))

    outfi=open(outf, 'w')
    nuncl=0
    ntot=0
    for record in SeqIO.parse(prot, 'fasta'):
        id=record.id
        ntot+=1
        idg=re.sub('\|.*', '', id)
        if idg not in cluster:
            nuncl+=1
            SeqIO.write(record, outfi, 'fasta')

    print('Wrote {:,} of {:,} unclustered proteins to "{}"'.format(nuncl, ntot, outf))
# --------------------------------------------------
if __name__ == '__main__':
    main()

