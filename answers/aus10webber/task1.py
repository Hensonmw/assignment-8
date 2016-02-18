#!/usr/bin/env python
# utf-8

"""
BIOL 7800 Assignment 8, Task 1
Austen T. Webber
2016_2_17
"""


def vols(x):
# Calculte integers from 0 to 1000
    while x>=0 and x<1001:
        y=((x*(x+1))/2)
        x=x+1
        vols(x)
        return y

def main():
    y=vols(1000)
    print(y)

if __name__ == '__main__':
     main()

#http://stackoverflow.com/questions/12082442/pythonhow-to-make-the-sum-of-the-values-of-a-while-loop-store-into-a-variable      
