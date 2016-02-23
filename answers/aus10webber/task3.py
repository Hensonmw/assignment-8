#!/usr/bin/env python
# utf-8

"""
BIOL 7800 Assignment 8, Task 3
Austen T. Webber
2016_2_17
"""

def function_1(x):
    for letters in x:
        letters = x[::-1]
    print(letters)


def function_2(sec):
    for y, z in sec.items():
        print(y, z)


def function_3(seq):
    for seq in ("ATGGCATCCGACGCTAGCGACTCGACTCGACTACGACGCTCTCTC"):
        print(seq)


def function_4():
    for w in range(0,23):
        print(w)


def function_5(file):
    with open(file) as truth:
        for line in truth:
            print(line)


def main():
    x= input('What word do you want reversed?: ')
    function_1(x)
    print('\r\n')

    sec = {'Tennessee' : 'Volunteers', 'LSU' : 'Tigers', 'Georgia' : 'Bulldogs',
    'Alabama' : 'Crimson Tide', 'Auburn' : 'Tigers', 'Texas A&M' : 'Aggies',
    'Missouri' : 'Tigers', 'Kentucky' : 'Wildcats', 'Florida' : 'Gators',
    'South Carolina' : 'Gamecocks', 'Vanderbilt' : 'Commodores',
     'Arkansas' : 'Razorbacks','Mississippi' : 'Rebel Black Bears',
     'Mississippi State' : 'Bulldogs'}
    print("SEC teams")
    print('\r\n')
    function_2(sec)
    print('\r\n')

    seq = ("ATGGCATCCGACGCTAGCGACTCGACTCGACTACGACGCTCTCTC")
    print("Function 3")
    function_3(seq)
    print('\r\n')

    print("Function 4")
    function_4()
    print('\r\n')

    print("Function 5")
    # You may need to change the path of the file
    function_5('est.txt')
    # function_5('C:/Users/Austen/Desktop/BIOL 7800/Assignment 8/est.txt')


if __name__ == '__main__':
    main()
