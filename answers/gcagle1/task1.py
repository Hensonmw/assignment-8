#! /usr/bin/env python
# encoding: utf-8

'''
Compute the sum of 0 to 1000 (inclusive) in a function using while.
Return the sum of these numbers to the main loop and print the result.
'''


def task1():
    count = 0
    i = 0
    while i < 1001:
        count += i
        i += 1
    else:
        return count


def main():
    task1()
    print(task1())

if __name__ == '__main__':
    main()
