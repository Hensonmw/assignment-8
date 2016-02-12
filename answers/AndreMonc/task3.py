# !/usr/bin/env python
# encoding: utf-8

"""
My for-loops program
Created by Andre Moncrieff on 12 Feb 2016.
Copyright 2016 Andre E. Moncrieff. All rights reserved.
"""

import array


def for_list():
    fixed_list = []
    for word in ["bro", "mo", "fa", "ga", "te", "wea", "hea", "la", "smo",
                 "bo", "hi", "nei", "ra"]:
        word += "ther"
        fixed_list.append(word)
    return fixed_list


def for_tuple():
    tup = ([1, 2, 3], [3, 2, 1], [4, 5, 6])
    for num in tup:
        num.append(5)
    return tup


def for_array():
    the_array = array.array('L', [1, 1, 1, 1, 1, 1])
    for int in range(len(the_array) - 1):
        the_array.insert(int, 5)
    return the_array


def for_dict(letter):
    names_nicknames = {
            "Andre": "Dre",
            "Jonathan": "Jonnyboy",
            "Nathaniel": "Nate",
            "Samantha": "Sam",
            "Daniel": "Danny",
            "Rachelle": "Shelly",
            "Brenton": "Brent",
            "Brant": "Brant",
            "Theodore": "Ted"}
    for name in names_nicknames.keys():
        if names_nicknames[name][-1:] == "d":
            names_nicknames[name] += "d"
        if names_nicknames[name][-1:] == "m":
            names_nicknames[name] += "m"
        if names_nicknames[name][-1:] != "y":
            names_nicknames[name] += "y"
    return names_nicknames


def for_string():
    seq = "ATGCTGACNATNNNNTCCTTTT"
    seq_list = []
    for base in seq:
        if base != "N":
            seq_list.append(base)
    return seq_list


def main():
    fin_list = for_list()
    print("\nFixed list: \n", fin_list)
    fin_tup = for_tuple()
    print("\nAdjusted tuple: \n", fin_tup)
    fin_array = for_array()
    print("\nAdjusted array: \n", fin_array)
    fin_dict = for_dict("S")
    print("\nNames nad diminutive nicknames: \n", fin_dict)
    fin_seq = for_string()
    print("\nA list output after iterating over string: \n", fin_seq)


if __name__ == '__main__':
    main()
