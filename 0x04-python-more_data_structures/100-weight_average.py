#!/usr/bin/python3
def weight_average(my_list=[]):
    top = sum([x * y for x, y in my_list])
    bottom = sum([y for x, y in my_list])
    return top/bottom
