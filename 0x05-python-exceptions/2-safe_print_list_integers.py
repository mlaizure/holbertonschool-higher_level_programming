#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    num_printed = 0
    for idx in range(x):
        try:
            print("{:d}".format(my_list[idx]), end="")
        except (ValueError, TypeError):
            pass
        except IndexError:
            raise
        else:
            num_printed += 1
    print()
    return num_printed
