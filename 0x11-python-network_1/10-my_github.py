#!/usr/bin/python3
"""taks GitHub credentials and uses API to display id"""
if __name__ == "__main__":
    import requests
    from sys import argv

    r = requests.get('https://api.github.com/user', auth=(argv[1], argv[2]))
    print(r.json().get('id'))
