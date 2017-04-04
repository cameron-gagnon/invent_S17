#!/usr/bin/env python3.5

import re
import requests
import sys
from pprint import pprint

CONTEXT = 20

def main():
    # get the link from the user
    link = get_link()
    # get the source code of the page
    source_code = grabber(link)
    # get the phrase we want to search for from our user
    phrase = get_search_phrase()
    # search through the webpage for that phrase
    search_for_phrase(source_code, phrase)

def get_search_phrase():
    """ Returns the search phrase from the user """
    return input("Please provide a phrase to search for: ")

def search_for_phrase(source_code, phrase):
    """ Searches for the phrase the user specified. If the phrase is found,
    print CONTEXT number of characters that surround the search phrase """
    pattern = ".{{{0}}}{1}.{{{0}}}".format(CONTEXT, phrase)
    res = re.findall(pattern, source_code, re.IGNORECASE)

    display_results(res, phrase)

def display_results(res, phrase):
    """ Print out the results if there was a match, otherwise inform the user
    that their result wasn't found """
    if len(res) > 0:
        print("Here are your results for {}!".format(phrase))
        pprint(res)
    else:
        print("Sorry! {} does not appear in this webpage :(".format(phrase))

def grabber(link):
    """ Return the HTML of a webpage """
    response = requests.get(link)
    return response.text

def get_link():
    """ Return the link the user wants to search through """
    # print the intro of this program
    print_intro()
    return input("Enter the link here: ")

def print_intro():
    print("Hello! This program will search through a webpage for a term you give "
    "me! Then, I'll show you what I find! To get started, enter a link you would "
    "like to search through (make sure it has http:// or https:// in front of "
    "it)")

if __name__ == "__main__":
    main()
