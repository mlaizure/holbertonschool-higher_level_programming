#!/usr/bin/python3
"""sends request to URL and displays value of X-Request-Id"""
if __name__ == "__main__":
    from urllib import request
    from sys import argv

    with request.urlopen(argv[1]) as f:
        print("{}".format(f.headers['X-Request-Id']))
