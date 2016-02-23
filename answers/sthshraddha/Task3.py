#!/usr/bin/env python

"""

Task 3:
In Python, we tend to use for loops over different types of iterators much more
than while loops - they're more flexible and iterators are everywhere in
Python. Write a program that includes 5 different functions, each of which
should demonstrate the use of for over different types of iterators. Your
program should include these five functions, a main() function that calls all
the other functions, and the ifmain statement.

Created by Shraddha Shrestha on February 12, 2016.
Copyright 2016 Shraddha Shrestha. All rights reserved.

"""


def search(haystack, needle):
    # example for string using "for" loop
    for x in (haystack):
        if x == needle:
            return "yay,found"
    return "not found"


def mytotalexpense(expenses):
    # example for dictionary using "for" loop
    total_expense = 0
    expense_items = expenses.items()
    # converting dictionary to list
    for k, v in expense_items:
        # k=key,v=value
        total_expense = total_expense + v
        # print(k)
        # print(v)
        # print(total_expense)
    return total_expense


def sum_list():
    # example for list using "for" loop
    list1 = [1, 2, 3, 4, 5]
    list2 = [6, 7, 8, 9, 10]
    list3 = []
    index = -1
    for value in list1:
        index = index + 1
        # Here value is the first item in list1
        list3.append(value + list2[index])
        # print(value)
        # print(index)
    return list3


def for_tuple(x):
    # counting the alphabet in the tuple using "for" loop
    my_tuple = ("e", "p", "s", "a", "h", "m", "a", "l", "l", "a")
    count = 0
    for item in my_tuple:
        if item == x:
            count += 1
    return count


def for_file():
    # this prints out the words in each line of the text file.
    # backslash at the end of line means continuation.
    count = 0
    input_file = open("C:\\Users\\Shraddha\\Desktop\\assignment-8\\answers\\sthshraddha\
\\eight.txt")
    for line in input_file:
        count += 1
    return count


def main():
    search_result = search('shraddha', 'a')
    print("\nDid it find the needle? \n", search_result)
    expenses = {"rent": 660, "gas": 50, "food": 250, "miscellaneous": 240}
    monthly_expense = mytotalexpense(expenses)
    print("\nEstimated monthly expense:\n", monthly_expense)
    two_list_sum = sum_list()
    print("\nSum of two lists: \n", two_list_sum)
    count_item = for_tuple("a")
    print("\nNumber of given item in tuple above: \n", count_item)
    lines_of_file = for_file()
    print("\nNumber of lines in the given file: \n", lines_of_file)


if __name__ == '__main__':
    main()
