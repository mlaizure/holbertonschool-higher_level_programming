#!/usr/bin/python3
"""script that fetches a URL"""
if __name__ == "__main__":
    from urllib import request

    with request.urlopen('https://intranet.hbtn.io/status') as f:
        content = f.read()
        print(f.headers)
        print("Body response:")
        print("\t- type: {}".format(type(content)))
        print("\t- content: {}".format(content))
        print("\t- utf8 content: {}".format(content.decode('utf-8')))
