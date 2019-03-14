#!/usr/bin/env python3
"""
Author : pmoma
Date   : 2019-03-16
Purpose: Annotate BLAST output
"""

import argparse
import sys
import os
import csv
from collections import defaultdict

# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Annotate BLAST output',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        'FILE', metavar='FILE', help='BLAST output (-outfmt 6)')

    parser.add_argument(
        '-a',
	'--annotations',
        help='Annotation file',
        metavar='FILE',
        type=str,
        default='')

    parser.add_argument(
        '-o',
	'--outfile',
        help='Output file',
        metavar='FILE',
        type=str,
        default='')

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
    file = args.FILE
    annt = args.annotations
    outf = args.outfile
    
    if not os.path.isfile(file):
        die('"{}" is not a file'.format(file))
    
    if not os.path.isfile(annt):
        die('"{}" is not a file'.format(annt))
        
    anntd={}
    counts = defaultdict(int)
    with open(annt) as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',')
        for row in reader:
            genus = row['genus'] if row['genus'] != "" else 'NA'
            species = row['species'] if row['species'] != "" else 'NA'
            centroid = row['centroid']
            anntd[centroid] = (genus, species)
#        print(anntd)    
    
    head='seq_id\tpident\tgenus\tspecies\n'
    if outf != '':
        out=open(outf,'wt')
        out.write('{}'.format(head))
    else:
        print(head, end='')
            
    with open(file, 'rt') as fil:
        for j in fil:
            tbfile=j.split('\t')
            seq_id=tbfile[1]
            pident=tbfile[2]
            search=anntd.get(seq_id, ["BAD", "BAD"])
            gen=search[0]
            spec=search[1]            
            if search[0] == "BAD":
                warn(msg="Cannot find seq {} in lookup".format(seq_id))
                continue
            
            if outf == "":
                print("{}\t{}\t{}\t{}".format(seq_id, pident, gen, spec))
            else:
                out.write("{}\t{}\t{}\t{}\n".format(seq_id, pident, gen, spec))

    if outf != "":
        out.close()
          

# --------------------------------------------------
if __name__ == '__main__':
    main()
