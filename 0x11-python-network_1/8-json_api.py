#!/usr/bin/python3
"""sends POST request to URL with the letter as a parameter"""
if __name__ == "__main__":
    import requests
    from sys import argv

    if len(argv) < 2:
        data = {"q": ""}
    else:
        data = {"q": argv[1]}

    r = requests.post('http://0.0.0.0:5000/search_user', data=data)
    try:
        json_resp = r.json()
        if json_resp == {}:
            print("No result")
        else:
            print("[{}] {}".format(json_resp['id'], json_resp['name']))
    except ValueError:
        print("Not a valid JSON")
