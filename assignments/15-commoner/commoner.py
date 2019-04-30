#!/usr/bin/env python3
"""
Author : pmoma
Date   : 2019-04-16
Purpose: Hamm
"""
import logging
import argparse
import sys
import re
import os
import itertools
from tabulate import tabulate
import io
# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Hamming Python script',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        'positionals', metavar='FILE', nargs=2, help='File inputs', type=argparse.FileType('r', encoding='UTF-8'))

    parser.add_argument(
        '-m',
        '--min_len',
        help='Minimum length of words',
        metavar='int',
        type=int,
        default=0)

    parser.add_argument(
        '-n',
        '--hamming_distance',
        help='Allowed Hamming distance',
        metavar='int',
        type=int,
        default=0)

    parser.add_argument(
        '-l',
        '--logfile',
        help='Logfile name',
        metavar='str',
        type=str,
        default='.log')

    parser.add_argument(
        '-d',
	    '--debug',
        help='Debug',
        default=False,
        action='store_true')

    parser.add_argument(
        '-t',
        '--table',
        help='Table output',
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
def dist(s1,s2):
    """Hamming code"""
    num= abs(len(s1)-len(s2))
    for l1, l2 in list(zip(s1,s2)):
        if l1!= l2:
            num+= 1

    logging.debug('s1 = {}, s2 = {}, d = {}'.format(s1,s2,num))
    return num

def test_dist():
    """dist ok"""

    tests = [('foo', 'boo', 1), ('foo', 'faa', 2), ('foo', 'foobar', 3),
             ('TAGGGCAATCATCCGAG', 'ACCGTCAGTAATGCTAC',
              9), ('TAGGGCAATCATCCGG', 'ACCGTCAGTAATGCTAC', 10)]

    for s1, s2, n in tests:
        d = dist(s1, s2)
        assert d == n

def uniq_words(fileh, min_len):
    words=fileh.read().split()
    words=[re.sub('[^a-zA-Z0-9]','', word).lower() for word in words]
    gwords=[]
    for i in words:
        if len(i)>=min_len and i not in gwords:
            gwords.append(i)
    return set(gwords)
"""Cough cough time for a new language cough cough"""

def test_uniq_words():
    """Test uniq_words"""

    s1 = '?foo, "bar", FOO: $fa,'
    s2 = '%Apple.; -Pear. ;bANAna!!!'

    assert uniq_words(io.StringIO(s1), 0) == set(['foo', 'bar', 'fa'])

    assert uniq_words(io.StringIO(s1), 3) == set(['foo', 'bar'])

    assert uniq_words(io.StringIO(s2), 0) == set(['apple', 'pear', 'banana'])

    assert uniq_words(io.StringIO(s2), 4) == set(['apple', 'pear', 'banana'])

    assert uniq_words(io.StringIO(s2), 5) == set(['apple', 'banana'])

def common(words1, words2, distance):
    gwords=[]
    for i in itertools.product(words1, words2):
        wdist = dist(i[0], i[1])
        if wdist<=distance:
            gwords.append((i[0], i[1], wdist))
    return sorted(gwords)

def test_common():
    w1 = ['foo', 'bar', 'quux']
    w2 = ['bar', 'baz', 'faa']

    assert common(w1, w2, 0) == [('bar', 'bar', 0)]

    assert common(w1, w2, 1) == [('bar', 'bar', 0), ('bar', 'baz', 1)]

    assert common(w1, w2, 2) == [('bar', 'bar', 0), ('bar', 'baz', 1),
                                 ('bar', 'faa', 2), ('foo', 'faa', 2)]
# --------------------------------------------------
def main():
    args = get_args()
    f1,f2=args.positionals
    mlen=args.min_len
    ndist=args.hamming_distance
    log=args.logfile
    debug=args.debug
    table=args.table

    logging.basicConfig(
    filename=log,
    filemode='w',
    level=logging.DEBUG if debug else logging.CRITICAL
)
    logging.debug('file1 = {}, file2 = {}'.format(os.path.basename(f1.name), os.path.basename(f2.name)))

    if ndist<0:
        die("--distance \"{}\" must be > 0".format(ndist))

    words1 = uniq_words(f1, mlen)
    words2 = uniq_words(f2, mlen)
    common_words = common(words1, words2, ndist)

    if len(common_words)==0:
        print('No words in common.')
    elif table:
        print(tabulate(common_words, ['word1', 'word2', 'distance'], tablefmt='psql'))
    else:
        print('word1\tword2\tdistance')
        for (w1, w2, d) in common_words:
            print('{}\t{}\t{}'.format(w1,w2,d))

# --------------------------------------------------
if __name__ == '__main__':
    main()

