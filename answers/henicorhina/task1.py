# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""
BIOL7800 assignment 8
Oscar Johnson 11 February 2016
"""


def sum1000():
    """
    sum all numbers from 1 to 1000
    """
    x = 0
    i = 0
    while i <= 1000:
        i += 1
        x += i
    return x

    
def main():
    x = sum1000()
    print(x)


if __name__ == '__main__':
    main()