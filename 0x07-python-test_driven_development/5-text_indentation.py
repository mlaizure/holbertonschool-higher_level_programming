#!/usr/bin/python3
"""Module has a function that prints a text with 2 new lines after
a period, question mark or colon"""


def text_indentation(text):
    """prints text (must be string) with 2 new lines after a period, question
    mark, or colon"""
    if not isinstance(text, str):
        raise TypeError('text must be a string')
    i = 0
    while i < len(text):
        print(text[i], end="")
        if text[i] == '.' or text[i] == '?' or text[i] == ":":
            print('\n')
            if i < len(text) - 1 and text[i+1] == " ":
                i += 1
        i += 1
