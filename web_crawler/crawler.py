#!/usr/bin/env python3

from bs4 import BeautifulSoup
from collections import defaultdict
import re
import requests
import sys
from time import sleep

MAX_LINKS_TO_CRAWL = 1000000 # 1 million

def get_website_html(url):
    """ Get the HTML of a single website """
    try:
        return requests.get(url).text

    except Exception as e:
        print("\tCould not visit: {}".format(url))
        return ""

def get_all_links_from_html(html):
    """ Return all the links found within an HTML page """
    # BeautifulSoup makes HTML easy to parse and find things we want.
    # In this case it makes it easy to find links within pages
    soup = BeautifulSoup(html, "html.parser")
    links_to_return = []
    for link in soup.find_all('a'):
        try:
            # make sure the link has the http protocal attached to it
            if re.search("http|https", link.get('href'), re.IGNORECASE):
                links_to_return.append(link.get('href'))
        except:
            # probably no href or an error when parsing the href link
            pass

    return links_to_return

def crawl(links_to_visit):
    """ Main crawling function that will maintain a list of links visited
    and go through and find new links in each page"""
    visited = defaultdict(bool)
    link_counter = 0
    log = open('link_trail.txt', 'w')

    try:
        while(len(links_to_visit) and link_counter <= MAX_LINKS_TO_CRAWL):
            link = links_to_visit.pop(0)
            # don't revisit links
            if visited[link]:
                print("Already visited link, continuing to next link...")
                continue

            visited[link] = True
            link_counter += 1

            print("Visiting: {}".format(link))
            log.write("{}\n".format(link))
            html = get_website_html(link)
            # add the links that we found to the list
            # of links we're going to crawl
            links_to_visit.extend(get_all_links_from_html(html))

        raise KeyboardInterrupt

    except KeyboardInterrupt:
        log.close()

        print("Exiting...")
        sys.exit(0)

def main():
    # get the url the user wants to start crawling at
    url = get_starting_url()
    crawl([url])

def print_info():
    print("This program crawls through webpages and will get all the links "
    "within the HTML and proceed to visit each of those links as well. To start "
    "things off, please give me a link to visit! (Make sure the link includes "
    "http:// or https://)")

def get_starting_url():
    print_info()
    return input("Enter link: ")

if __name__ == "__main__":
    main()
