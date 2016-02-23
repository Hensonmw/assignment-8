#!/usr/bin/env python
# utf-8

"""
Assignment 8
Task 2 Program: Summing with a for loop
Jessie Salter
12 February 2016
"""


def f_sum(x, y, z):
    '''This function uses a for loop to sum the numbers 1 to 1000'''
    for x in range(0, 1001):
        y = z - 1
        x += 1
        z = y + x
    return z


def main():
    print(f_sum(0, 0, 0))


if __name__ == '__main__':
    main()
