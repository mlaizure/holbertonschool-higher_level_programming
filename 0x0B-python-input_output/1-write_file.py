#!/usr/bin/python3
"""Module with function that writes a string to a text file and returns the
number of characters written"""


def write_file(filename="", text=""):
    """writes a string to a text file and returns the number of characters
    written"""
    with open(filename, mode='w', encoding='utf-8') as f:
        return f.write(text)


if __name__ == "__main__":
    write_file = __import__('1-write_file').write_file

    nb_characters = write_file("my_first_file.txt",
                               "Holberton School is so cool!\n")
    print(nb_characters)
