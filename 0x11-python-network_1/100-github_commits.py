#!/usr/bin/python3
"""takes GitHub credentials and uses API to display commits"""
if __name__ == "__main__":
    import requests
    from sys import argv

    url = 'https://api.github.com/repos/{}/{}/commits'.format(argv[2], argv[1])
    r = requests.get(url)
    commits = r.json()

    for idx, commit in enumerate(commits):
        print("{}: {}".format(commit.get('sha'),
                              commit.get('commit').get('author').get('name')))
        if idx == 9:
            break
