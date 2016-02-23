#!/usr/bin/env python

"""

Task 1:
Previously, you wrote a program that used a recursive function to compute the
sum of the integers from 0 to 1000 (inclusive). This time, I want you to
accomplish the same thing, but using a while loop. Compute the sum of 0 to 1000
(inclusive) in a function using while. Return the sum of these numbers to the
main loop and print the result. Write the program to include a main()
function and the ifmain statement.

Created by Shraddha Shrestha on February 12, 2016.
Copyright 2016 Shraddha Shrestha. All rights reserved.

"""


def sum_of_integer(start, end):
#this returns sum of integers in a given range using "while loop".
    result = 0
    i = 0 #counter
    while i < end:
        result += i
        i += 1
    return result


def main():
    answer = sum_of_integer(0, 1001)
    print(answer)


if __name__ == '__main__':
    main()
