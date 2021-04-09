#!/usr/bin/python3
"""sends request to URL and displays body of response"""
if __name__ == "__main__":
    from urllib import request
    from sys import argv

    try:
        with request.urlopen(argv[1]) as f:
            print(f.read().decode('utf-8'))
    except request.HTTPError as exception:
        print("Error code: {}".format(exception.code))
