#!/usr/bin/python3
"""module with find_peak function"""


def find_peak(list_of_integers):
    """finds a peak in unsorted ints"""
    if not list_of_integers:
        return "None"
    return list_of_integers[
        find_peak_help(list_of_integers, 0, len(list_of_integers) - 1)]


def find_peak_help(il, low, high):
    """finds the peak"""
    ln = len(il)
    mid = int(low + (high - low)/2)
    if ((mid == 0 or il[mid - 1] <= il[mid]) and
       (mid == ln - 1 or il[mid + 1] <= il[mid])):
        return mid
    elif (mid > 0 and il[mid - 1] > il[mid]):
        return find_peak_help(il, low, mid - 1)
    else:
        return find_peak_help(il, mid + 1, high)
