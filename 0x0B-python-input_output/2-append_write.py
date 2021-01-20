#!/usr/bin/python3
"""Module with function that appends a string at the end of a text file
(UTF8) and returns the number of characters added"""


def append_write(filename="", text=""):
    """function that appends a string at the end of a text file(UTF8) and
    returns the number of characters added"""
    with open(filename, mode='a', encoding='utf-8') as f:
        return f.write(text)

if __name__ == "__main__":
    append_write = __import__('2-append_write').append_write

    nb_characters_added = append_write("file_append.txt",
                                       "Holberton School is so cool!\n")
    print(nb_characters_added)
