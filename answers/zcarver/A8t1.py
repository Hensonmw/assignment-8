#!/usr/bin/env python
#encoding UTF-8

'''
Assignment8Task1 biol7800
ZacCarver 02/16/2016
Task1-using 'while' loop the sum 0-1000 and return this value using ifmain
main().
'''


def sw():
    s = 0
    i = 0
    while i <= 1000:
        i += 1
        s += 1
    return s


def main():
    s = sw()
    print(s)

if __name__ == '__main__':
    main()
