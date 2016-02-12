# !/usr/bin/env python
# encoding: utf-8


"""
My while-loop summation program
Created by Andre Moncrieff on 12 Feb 2016.
Copyright 2016 Andre E. Moncrieff. All rights reserved.
"""

import argparse


def parser():
    """
    Create argument input
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("upper_limit", help="Input the upper inclusive limit" +
                        " of the summation between 0 and the input value",
                        type=int)
    args = parser.parse_args()
    return args.upper_limit


def while_summation(upper_lim):
    """
    Sums all numbers between 0 and upper_lim (upper_lim is inclusive)
    """
    counter = 0
    total = 0
    while counter < upper_lim:
        counter += 1
        total += counter
    return total


def main():
    total = while_summation(upper_lim=parser())
    print(total)


if __name__ == '__main__':
    main()
