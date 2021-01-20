#!/usr/bin/python3
"""Module with class MyList that inherits from list"""


class MyList(list):
    """class that inherits from list with method that prints the list in
    ascending order"""

    def print_sorted(self):
        """prints the list in ascending order"""
        print(sorted(self))

if __name__ == "__main__":
    MyList = __import__('1-my_list').MyList

    my_list = MyList()
    my_list.append(1)
    my_list.append(4)
    my_list.append(2)
    my_list.append(3)
    my_list.append(5)
    print(my_list)
    my_list.print_sorted()
    print(my_list)
