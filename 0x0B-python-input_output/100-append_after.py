#!/usr/bin/python3
"""Module with function that inserts a line of text to a file, after each
line containing a specific string"""


def append_after(filename="", search_string="", new_string=""):
    """inserts a line of text to a file, after each line containing a
    specific string"""
    with open(filename, encoding='utf-8') as f:
        contents = f.readlines()

        for idx, line in enumerate(contents):
            if search_string in line:
                contents.insert(idx + 1, new_string)
        contents = "".join(contents)

    with open(filename, mode='w', encoding='utf-8') as f:
        f.write(contents)
