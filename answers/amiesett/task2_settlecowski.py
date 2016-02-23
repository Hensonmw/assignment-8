#!/usr/bin/env python
# encoding: utf-8

"""
BIOL7800 Assignment 8 Task 2

Amie Settlecowski
16 Feb. 2016

This program sums integers [0,1000] using a for loop
"""


def sigma(i=0, n=1000):
    # returns sum of [i,n] using for loop
    summ = 0
    for integer in range(i, (n+1)):
        summ += integer
    return summ


def main():
    summ = sigma()
    print(summ)

if __name__ == '__main__':
    main()
