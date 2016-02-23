#!/usr/bin/env python
# utf-8

"""
Assignment 8, Task 1
Jon Nations on 14 February 2016

"""


def toops(tup):
    for tup, item in enumerate(tup, start=0):
        print(tup, item)


def strang(words):
    for x in words:
        print(x)


def listy(lost):
    for x in lost:
        print(x[7:])


def diction(fooddict):
    for z, v in fooddict.items():
        print(z, v)


def intijars():
    for x in range(10, 11):
        if x == 10:
            print("Multiplication of 10 x 10 = ", x * x)
        else:
            print(x)


def main():
    tup = ("1, 2", "3, 4", "5, 6")
    print("TUPLE FUNCTION")
    toops(tup)

    words = ("the bird is the word")
    print("STRING FUNCTION")
    strang(words)

    lost = ['do not print', 'do not this']
    print("LIST FUNCTION")
    listy(lost)

    fooddict = {'apple': 'red', 'orange': 'orange', 'banana': 'yellow'}
    print("DICTIONARY FUNCTION")
    diction(fooddict)

    print("INTEGER FUNCTION")
    intijars()

if __name__ == '__main__':
    main()
