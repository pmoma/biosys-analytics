#!/usr/bin/env python3
"""test for open.py"""

from subprocess import getstatusoutput, getoutput
import os.path
import re

open = './open.py'

def test_exists():
    """scripts exist"""
    assert os.path.exists(open)

def test_usage():
    """usage"""
    (retval, out) = getstatusoutput(open)
    assert retval > 0
    assert re.match("usage", out, re.IGNORECASE)

def test_word1():
    """runs test1"""
    out1 = getoutput(open + ' Foo')
    assert out1.rstrip() == 'FFoFoo'

def test_word2():
    """runs test2"""
    out1 = getoutput(open + ' Python')
    assert out1.rstrip() == 'PPyPytPythPythoPython'

def test_word3():
    """runs test3"""
    out1 = getoutput(open + ' foobarbaz')
    assert out1.rstrip() == 'ffofoofoobfoobafoobarfoobarbfoobarbafoobarbaz'

