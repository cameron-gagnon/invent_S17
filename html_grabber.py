#!/usr/bin/env python3.5

import requests
import sys

def grabber(link):
    response = requests.get(link)
    print(response.text)

def get_link():
    if len(sys.argv) <= 1:
        print("Please provide a link to get the HTML of like this:")
        print("\tpython3 html_grabber.py https://google.com")
        sys.exit(1)
    else:
        return sys.argv[1]

if __name__ == "__main__":
    link = get_link()
    grabber(link)
