#!/usr/bin/env python
# utf-8

"""
Assignment 8, Task 1
Jon Nations on 14 February 2016
Adapted from BIOL7800 Lecture found at
https://github.com/biolprogramming/syllabus/blob/master/lectures/Lecture7.pdf

"""


def summation(x=0):
    i = 0
    while i < 1000:
        i += 1
        x += i
    return x


def main():
    print(summation(x=0))


if __name__ == '__main__':
    main()
