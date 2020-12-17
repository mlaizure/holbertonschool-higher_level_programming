#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or not isinstance(roman_string, str):
        return 0
    r_dict = dict(I=1, V=5, X=10, L=50, C=100, D=500, M=1000)
    nums = [r_dict[c] for c in roman_string]
    return nums[-1] + sum([n * -1 if nums[idx+1] > n else n
                           for idx, n in enumerate(nums[:-1])])
