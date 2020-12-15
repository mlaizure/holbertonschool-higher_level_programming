#!/usr/bin/python3
def no_c(my_string):
    if my_string:
        my_list = list(my_string)
        for i in my_list:
            if i == 'c':
                my_list.remove('c')
            if i == 'C':
                my_list.remove('C')
        new_str = ""
        return new_str.join(my_list)
