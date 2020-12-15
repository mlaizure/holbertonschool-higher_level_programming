#!/usr/bin/python3
def no_c(my_string):
    new_str = ""
    if my_string:
        my_list = list(my_string)
        for i in my_list:
            if i == 'c':
                my_list.remove('c')
            if i == 'C':
                my_list.remove('C')
        return new_str.join(my_list)
    else:
        return new_str
