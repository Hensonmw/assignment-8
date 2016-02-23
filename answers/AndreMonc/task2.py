# !/usr/bin/env python
# encoding: utf-8


"""
My for-loop summation program
Created by Andre Moncrieff on 12 Feb 2016.
Copyright 2016 Andre E. Moncrieff. All rights reserved.
"""

import argparse


def parser():
    """
    Create argument input
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("upper_limit", help="Input the upper non-inclusive" +
                        " limit of the summation between 0 and the input value"
                        , type=int)
    args = parser.parse_args()
    return args.upper_limit


def for_summation(upper_lim):
    """
    Sums all numbers between 0 and upper_lim (upper_lim is exclusive)
    """
    total = 0
    for num in range(0, upper_lim):
        total += num
    return total


def main():
    total = for_summation(parser())
    print(total)


if __name__ == '__main__':
    main()
