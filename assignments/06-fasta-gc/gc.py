#!/usr/bin/env python3
"""
Author : pmoma
Date   : 2019-02-28
Purpose: Fasta parsing
"""

from collections import Counter
from Bio import SeqIO
import argparse
import sys
import os
import shutil

# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Fasta parser for GC content',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        'fasta', metavar='FILE', nargs='+', help='FASTA file(s)')

    parser.add_argument(
        '-o',
	'--outdir',
        help='Output directory',
        metavar='DIR',
        type=str,
        default='out')

    parser.add_argument(
        '-p',
	'--pct_gc',
        help='Dividing line for percent GC',
        metavar='int',
        type=int,
        default=50)

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
    pgc = args.pct_gc
    odir = args.outdir
    fasta = args.fasta
       
    if not 1 <= pgc <= 100:
        die('--pct_gc "{}" must be between 0 and 100'.format(pgc))
    scount=0
    
    if os.path.exists(odir):
        shutil.rmtree(odir)
    os.makedirs(odir)
    
    for num, file in enumerate(fasta,start=1):
        if not os.path.isfile(file):
            warn('"{}" is not a file'.format(file))
            continue
        bn=os.path.basename(file)
        fh=os.path.splitext(bn)
        print(fh[0])
        print('{}: {}'.format(num,bn))
        
        highp=open(os.path.join(odir,(fh[0]+'_high'+fh[1])), 'wt')
        lowp=open(os.path.join(odir,(fh[0]+'_low'+fh[1])), 'wt')
        with open(file) as fil:
            for record in SeqIO.parse(fil, 'fasta'):
#                print(record.seq)
                seq_len=len(record.seq)
                nucs=Counter(record.seq)
                gcnum=nucs.get('G',0)+nucs.get('C',0)
                gc=(int(gcnum/seq_len * 100))
                
                if gc>=pgc: 
                    SeqIO.write(record, highp,'fasta')
                else: 
                    SeqIO.write(record,lowp,'fasta')
                scount+=1             
            
    print('Done, wrote {} sequences to out dir "{}"'.format(scount, odir))

# --------------------------------------------------
if __name__ == '__main__':
    main()

