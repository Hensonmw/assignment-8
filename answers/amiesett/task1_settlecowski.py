#!/usr/bin/env python
# encoding: utf-8

"""
BIOL7800 Assignment 8 Task 1

Amie Settlecowski
16 Feb. 2016

This program sums integers [0,1000] using a while loop
"""


def sigma(i=0, n=1000):
    # returns sum of [i,n] using while loop
    summ = 0
    while i <= n:
        summ += i
        i += 1
    return summ


def main():
    summ = sigma()
    print(summ)

if __name__ == '__main__':
    main()
