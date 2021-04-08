#!/usr/bin/python3
"""module with find_peak function"""

def find_peak(list_of_integers):
    """finds a peak in unsorted ints"""
    if not list_of_integers:
        return "None"
    for idx, num in enumerate(list_of_integers):
        if idx == 0:
            if num > list_of_integers[1]:
                return num
        if idx == len(list_of_integers) - 1:
            return num
        if num > list_of_integers[idx - 1] and num > list_of_integers[idx + 1]:
            return num
