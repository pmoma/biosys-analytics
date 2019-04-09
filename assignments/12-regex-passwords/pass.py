#!/usr/bin/env python3
"""
Author : pmoma
Date   : 2019-04-09
Purpose: Passwords
"""

import sys
import os
import re

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
    args=sys.argv

    if len(args) != 3:
        print('Usage: {} PASSWORD ALT'.format(os.path.basename(sys.argv[0])))
        sys.exit(1)

    pword=args[1]
    alt=args[2].lower()
#    print(pword,alt)
    phrase='nah'
    passphrase=re.compile('.?'+pword+'.?')

    if pword==alt or passphrase.match(alt) is not None or re.match(pword,alt,re.IGNORECASE):
        phrase='ok'


    print('{}'.format(phrase))

# --------------------------------------------------
if __name__ == '__main__':
    main()

