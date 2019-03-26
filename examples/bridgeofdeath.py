#!/usr/bin/env python3
"""
Author : pmoma
Date   : 2019-02-12
Purpose: Rock the Casbah
"""

import os
import sys


# --------------------------------------------------
def main():
    answers = {}
    for thing in ['name', 'quest', 'favorite color']:
        answer = input('What is your {}? '.format(thing))
        print(answer)
        answers[thing] = answer
    print(answers)
    

# --------------------------------------------------
main()
