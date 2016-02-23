#!/usr/bin/env python
# utf-8

"""
Program to calculate sum of numbers from 0 t0 1000 using for
Created by Pramod Pantha on 13 Feb, 2016.
Copyright 2016 Pramod Pantha. All right reserved.
"""


def sum1000():
    #gives sum of numbers from 0 to 1000 inclusive

    x = 0
    for num in range(1001):
        x += num
    return x


def main():
    x = sum1000()
    print(x)


if __name__ == '__main__':
    main()
