#!/usr/bin/python3
"""sends POST request to URL with email as a parameter"""
if __name__ == "__main__":
    import requests
    from sys import argv

    data = {"email": argv[2]}
    r = requests.post(argv[1], data=data)
    print(r.text)
