#!/usr/bin/python3
def uppercase(str):
    for letter in str:
        n = ord(letter)
        if ord('a') <= n <= ord('z'):
            n_upper = n - (ord('a') - ord('A'))
        else:
            n_upper = n
        print("{}".format(chr(n_upper)), end="")
    print()
