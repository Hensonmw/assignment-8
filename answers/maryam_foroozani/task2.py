#!/usr/bin/env python
# encoding: utf-8
"""
created by me for task2
"""


def sum_function():
    """
     compute the sum of the integers from 0 to 1000 (inclusive) with for loop
    """
    s = 0
    for i in range(1001):
        s += i
    return s


def main():
    result = sum_function()
    print(result)

if __name__ == '__main__':
    main()
