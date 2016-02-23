#!/usr/bin/env python
# encoding: utf-8

"""
Iteration Assignment

Task 3

Elisa Elizondo
"""


def iterate_string():
    for x in 'string':
        print(x)

def iterate_list():
    L = [1, 2, 3, 4]
    for x in L:
        print(x)

def iterate_tuple():
    T = ("cat", "dog", "mouse", "bird")
    for x in T:
        print(x)

def iterate_dictionary():
    spots= {"cheetah":1, "leopard": 2, "jaguar":3}
    for x in spots:
        print(x)


def iterate_range():
    for i in range(12,15):
        print(i)


def main():
    iterate_string()
    iterate_list()
    iterate_dictionary()
    iterate_tuple()
    iterate_range()


if __name__ == '__main__':
    main()
