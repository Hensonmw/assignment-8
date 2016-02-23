#! /usr/bin/env python
# encoding: utf-8

'''
Compute the sum of 0 to 1000 (inclusive) in a function using for.
Return the sum of these numbers to the main loop and print the result.
'''


def task2():
    count = 0
    for i in range(0, 1001):
        count += i
    return count


def main():
    task2()
    print(task2())

if __name__ == '__main__':
    main()
