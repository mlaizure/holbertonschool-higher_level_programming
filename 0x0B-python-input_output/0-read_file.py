#!/usr/bin/python3
"""Module with function that reads a UTF8 text file and prints it to
stdout"""


def read_file(filename=""):
    """function that reads a UTF8 text file and prints it to stdout"""
    with open(filename, encoding='utf-8') as f:
        print(f.read(), end="")


if __name__ == "__main__":
    read_file = __import__('0-read_file').read_file

    read_file("my_file_0.txt")
