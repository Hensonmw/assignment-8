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
    for num in range(1001):
        x += num
    return x

    
def main():
    x = sum1000()
    print(x)


if __name__ == '__main__':
    main()