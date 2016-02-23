#!/usr/bin/env python
# utf-8

"""
Assignment 8
Task 1 Program: Summing with a while loop
Jessie Salter
12 February 2016
"""


def w_sum(x, y, z):
    '''This function uses a while loop to sum the number 0 to 1000'''
    while x <= 1000:
        y = z - 1
        x += 1
        z = y + x
    return z


def main():
    print(w_sum(0, 0, 0))


if __name__ == '__main__':
    main()
