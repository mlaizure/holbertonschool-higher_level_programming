#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    num_printed = 0
    for idx, element in enumerate(my_list):
        if idx < x:
            try:
                print(element, end="")
            except IndexError:
                pass
            else:
                num_printed += 1
    print()
    return num_printed
