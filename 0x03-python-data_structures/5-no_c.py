#!/usr/bin/python3
def no_c(my_string):
    if my_string:
        my_list = list(my_string)
        while 'c' in my_list:
            my_list.remove('c')
        while 'C' in my_list:
            my_list.remove('C')
        return "".join(my_list)
    else:
        return my_string
