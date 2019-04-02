#!/usr/bin/env python3
"""
Author : pmoma
Date   : 2019-04-02
Purpose: date parsing/formatting
"""
import re
import argparse
import sys

# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Date formatter',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        'date', metavar='DATE', help='The date to convert to standard "YYYY-MM-DD" format')

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
    date = args.date

#    print(date)
    hit=re.match('(?P<day>\d{1,2})', '01')
#    print(hit.group('day'))
    form1=re.compile('(?P<year>\d{4})-*(?P<month>\d{1,2})-*(?P<day>\d{1,2})?')
    form2=re.compile('(?P<month>\w{3,9})(-|(, ))(?P<year>\d{4})')
    form3=re.compile('(?P<month>\d{1,2})[/](?P<year>\d{2})')

    # form1=re.compile('(?P<year>\d{4})-*(?P<month>\d{1,2})-*(?P<day>\d{1,2})?')
    # form2=re.compile('(?P<month>\w{3,9})(-|(, ))(?P<year>\d{4})(-|(, ))(?P<day>\d{1,2})?')
    # form3=re.compile('(?P<month>\d{1,2})[/](?P<year>\d{2})[/](?P<day>\d{1,2})?')

    hit=form1.match(date) or form2.match(date) or form3.match(date)
#    print(hit.group('month'))
    #print(hit)
    if hit is None:
        die('No match')
    if len(hit.group('year'))==2:
        year='20'+hit.group('year')
    else:
        year=hit.group('year')
    mshort={'Jan':'01', 'Feb':'02', 'Mar':'03', 'Apr': '04', 'May':'05','Jun':'06','Jul':'07','Aug':'08','Sep':'09', 'Oct':'10','Nov':'11','Dec':'12'}
    mlong={'January':'01', 'February':'02', 'March':'03', 'April': '04', 'May':'05','June':'06','July':'07','August':'08','September':'09', 'October':'10','November':'11','December':'12'}
    if hit.group('month') in mshort.keys():
        month=mshort[hit.group('month')]
    elif hit.group('month') in mlong.keys():
        month=mlong[hit.group('month')]
    else:
        month=hit.group('month')
    if len(hit.group('month')) == 1:
        month='0'+hit.group('month')

    print(hit.groups())
    c=0
    # for i in hit.groups():
    #     m=re.match('[- ]',i)
    #     c+=1
    # print(c)
#    count the number of groups and remove the [-, None] so that there are three or two options
    # if hit.group('day'):
    #     print('yup')
    # else:
    #     day = '01'



    print('{}-{}-{}'.format(year,month,'01'))


# --------------------------------------------------
if __name__ == '__main__':
    main()

