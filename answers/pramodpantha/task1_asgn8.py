#!/usr/bin/env python
# utf-8

"""
Program to calculate sum of numbers from 0 t0 1000 using while
Created by Pramod Pantha on 13 Feb, 2016.
Copyright 2016 Pramod Pantha. All right reserved.
"""


def sum1000():
    #it gives sum of number from 0 to 1000
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
