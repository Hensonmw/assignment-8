#!/usr/bin/env python
# encoding: utf-8
"""
Iteration assignment.

Copyright 2016 Mukesh Maharjan. All rights reserved.
"""


def onetothau(x):
    """ Return the sum of 1+2+3 ... n """
    i = 1
    while i <= 1000:
        x += i
        i += 1
    return x


def main():
    print(onetothau(0))


if __name__ == '__main__':
    main()
