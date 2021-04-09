#!/usr/bin/python3
"""sends request to URL and displays value of X-Request-Id"""
if __name__ == "__main__":
    import requests
    from sys import argv

    r = requests.get(argv[1])
    print("{}".format(r.headers['X-Request-Id']))
