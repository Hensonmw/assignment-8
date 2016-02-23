#!/usr/bin/env python
#encoding UTF-8

'''
Assignment8Task2 biol7800
ZacCarver 02/16/2016
Task2-accomplish the same result as in A8T1 using the 'for' loop and return
using ifmain and main().
'''


def s2():
    s = 0
    for i in range(0-1001):
        s += i
    return s


def main():
    s = s2()
    print(s)

if __name__ == '__main__':
    main()
