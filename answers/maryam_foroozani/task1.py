#!/usr/bin/env python
# encoding: utf-8
"""
created by me for task2
"""


def sum_function():
    """
    compute the sum of the integers from 0 to 1000 (inclusive)
    """
    s = 0
    i = 1
    n = 1000
    while i <= n:
        s = s + i
        i = i + 1
    return (s)


def main():
    result = sum_function()
    print(result)

if __name__ == '__main__':
    main()
