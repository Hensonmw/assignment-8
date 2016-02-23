#!/usr/bin/env python
# encoding: utf-8
"""
created by me for task3
"""
import numpy as np


def for_list_index():
    """
    list as one of types of iterators
    """
    student_score = [90, 100, 87, 70, 88]
    for i, score in enumerate(student_score, 1):
        print(i, score)


def for_string():
    """
    String as one of types of iterators
    """
    the_string = "Python's strings have a handy method, split."
    words = the_string.split()
    for current_word in words:
        print(current_word)


def for_tuples():
    """
    Tuples as one of types of iterators
    """
    a = (1234, 4256, "hello")
    b = a, (1, 2, 3, 4)
    for i in b:
        print(i)


def for_dictionary():
    """
    Dictionary as one of types of iterators
    """
    student_scores = {"Ben": "100", "Rose": "95", "Mike": "80"}
    for student, scores in student_scores.items():
        print(student, "first score is", scores)


def for_array():
    """
    Array as one of types of iterators
    """
    a = np.array([1, 2, 3, 4])
    for i in a:
        print(i)


def main():
    for_list_index()
    for_string()
    for_tuples()
    for_dictionary()
    for_array()


if __name__ == '__main__':
    main()
