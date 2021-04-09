#!/usr/bin/python3
"""sends POST request to URL and displays body of response"""
if __name__ == "__main__":
    from urllib import request, parse
    from sys import argv

    data = parse.urlencode({"email": argv[2]}).encode()
    with request.urlopen(argv[1], data) as f:
        print("{}".format(f.read().decode('utf-8')))
