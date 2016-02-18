#!/usr/bin/env python
# utf-8

"""
BIOL 7800 Assignment 8, Task 2
Austen T. Webber
2016_2_17
"""

def loopyvol(i=0, n=1000):
# Find sum of 1 to 1000
    fi = 0
    for integer in range(i, (n+1)):
        fi += integer
    return fi


def main():
    fi = loopyvol()
    print(fi)

if __name__ == '__main__':
    main()

#http://stackoverflow.com/questions/23309657/python-total-sum-of-a-list-of-numbers-with-the-for-loop
