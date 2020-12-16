#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if my_list:
        truthy_list = []
        for i in my_list:
            if i % 2 == 0:
                truthy_list.append(True)
            else:
                truthy_list.append(False)
        return truthy_list
