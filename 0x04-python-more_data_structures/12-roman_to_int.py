#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or not isinstance(roman_string, str):
        return 0
    sum_roman = 0
    r_list = ["V", "X", "L", "C", "D", "M"]
    for i, c in enumerate(roman_string):
        if c == "V":
            sum_roman += 5
        elif c == "X":
            sum_roman += 10
        elif c == "L":
            sum_roman += 50
        elif c == "C":
            sum_roman += 100
        elif c == "D":
            sum_roman += 500
        elif c == "M":
            sum_roman += 1000
        elif c == "I" and i == len(roman_string) - 1:
            sum_roman += 1
        elif c == "I" and roman_string[i+1] not in r_list:
            sum_roman += 1
        else:
            sum_roman -= 1
    return sum_roman
