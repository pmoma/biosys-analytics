#!/usr/bin/env python3
"""
Author : pmoma
Date   : 2019-05-07
Purpose: Fasta uninterleaver
"""

import argparse
import sys
import itertools
import os

# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Split interleaved/paired reads',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        'file', metavar='FILE', help='Input file(s)', nargs='+')

    parser.add_argument(
        '-o',
	'--outdir',
        help='Output directory',
        metavar='DIR',
        type=str,
        default='split')

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
    outd = args.outdir


    c=0
    for i in file:
        if not os.path.isfile(i):
            warn('"{}" is not a file'.format(i))
            continue
        filename=outd+'/'+i
        if not os.path.exists(os.path.dirname(filename)):
            try:
                os.makedirs(os.path.dirname(filename))
            except OSError as exc: # Guard against race condition(I took this from the internet obviously but not trying to start a race war)
                if exc.errno != errno.EEXIST:
                    raise
        list1=[]
        list2=[]
        with open(i) as f:
            for line1,line2,line3,line4 in itertools.zip_longest(*[f]*4):
                #print(line1,line2,line3,line4)
                #print(filename)
                list1.append(line1)
                list1.append(line2)
                list2.append(line3)
                list2.append(line4)

        fname=os.path.basename(i)
        name=os.path.splitext(fname)
#        print(outd)
#        print(name[0])
        with open(outd+'/'+name[0]+'_1'+name[1],'w') as fw1:
            for item1 in list1:
                fw1.write(item1)
        with open(outd+'/'+name[0]+'_2'+name[1],'w') as fw2:
            for item2 in list2:
                fw2.write(item2)
        c+=1

        print('''   {}: {}
            split {} sequences to dir {}'''.format(c,i,len(list1), outd))


# --------------------------------------------------
if __name__ == '__main__':
    main()

