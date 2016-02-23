#!/usr/bin/env python
# encoding: utf-8
"""
Iteration assignment.

Copyright 2016 Mukesh Maharjan. All rights reserved.
"""


def mysum(xs):
    """ Sum all the numbers in the list xs, and return the total. """
    total = 0
    for x in xs:
        total = total + x
    return total


def main():
    print(mysum(range(1001)))


if __name__ == '__main__':
    main()
