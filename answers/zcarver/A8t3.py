#!/usr/bin/env python
#encoding UTF-8

'''
Assignment8Task3 biol7800
ZacCarver 02/16/2016
Task3-create 5fxns by using the 'for' loop over 5different iterators and call
these fxns back into main() using ifmain.
'''


def rf(w):
    for l in w:
        l = w[0]
        print(l)


def f(ls):
    for i in ls:
        i += 2
        print(i)


def ff(ex_file):
    f = open(ex_file, 'r')
    for line in f:
        print(line)


def rmv(string, n):
    begin = string[:n]
    end = string[n+1:]
    print(begin + end)


def utup(w):
    for value in w:
        print(value)


def main():
    w = input('some word: ')
    rf(w)
    # for a list
    ls = [5, 10, 15, 20]
    f(ls)
    # for a file
    ff('pkm.txt')
    # removes letter from string
    rmv("KYOGERE", 5)
    # unpacks tuple
    w = ("blue", "orb")
    utup(w)

if __name__ == '__main__':
    main()
