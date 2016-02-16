#!/usr/bin/env python

"""

Task 2:
Above, you wrote a program that used a while loop to compute the sum of the
integers from 0 to 1000 (inclusive). This time, I want you to accomplish the
same thing, but using a for loop. Compute the sum of 0 to 1000 (inclusive) in a
function using for. Return the sum of these numbers to the main loop and print
the result. Write the program to include a main() function and the ifmain
statement.

Created by Shraddha Shrestha on February 12, 2016.
Copyright 2016 Shraddha Shrestha. All rights reserved.

"""


def sum_of_integer(x=0):
#this returns sum of integers in a given range using "for loop".
    for i in range(0,1001):
        x += i
    return x


def main():
    answer = sum_of_integer(0)
    print(answer)


if __name__ == '__main__':
    main()
