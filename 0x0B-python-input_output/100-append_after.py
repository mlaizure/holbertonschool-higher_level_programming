#!/usr/bin/python3
"""Module with function that inserts a line of text to a file, after each
line containing a specific string"""


def append_after(filename="", search_string="", new_string=""):
    """inserts a line of text to a file, after each line containing a
    specific string"""
    with open(filename, encoding='utf-8') as f:
        contents = f.readlines()

    cpy = []
    for line in contents:
        cpy.append(line)
        if search_string in line:
            cpy.append(new_string)
    contents = "".join(cpy)

    with open(filename, mode='w', encoding='utf-8') as f:
        f.write(contents)
