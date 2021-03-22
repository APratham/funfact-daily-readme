#main.py
"""
Action script to select a random quote/fun-fact and put it on given repository's README.
"""

import os
import re
import sys
import random
import base64
from typing import List
from github import Github, GithubException

REPOSITORY = os.getenv("INPUT_REPOSITORY")
GH_TOKEN = os.getenv("INPUT_GH_TOKEN")
COMMIT_MSG = os.getenv("INPUT_COMMIT_MESSAGE")
OPTION = os.getenv("INPUT_OPTION")

QUOTES_PATH = "/quotes/quotes.txt"
FUNFACTS_PATH = "/funfacts/funfacts.txt"


def get_quotes() -> List[str]:
    """
    Get quotes from quotes/quotes.txt, return a list.
    """
    global QUOTES_PATH
    quotes = []
    with open(QUOTES_PATH, "r") as file:
        quotes.extend(file.readlines())
    random.shuffle(quotes)
    return quotes


def get_funfacts() -> List[str]:
    """
    Get funfacts from funfacts/funfacts.txt, return a list.
    """
    global FUNFACTS_PATH
    funfacts = []
    with open(FUNFACTS_PATH, "r") as file:
        funfacts.extend(file.readlines())
    random.shuffle(funfacts)
    return funfacts


def get_option_list(OPTION):
    """
    Utility to get text list for corresponding given option.
    """
    text_list = []
    if OPTION == 'quote':
        text_list.extend(get_quotes())
    elif OPTION == 'funfact':
        text_list.extend(get_funfacts())
    elif OPTION == 'both':
        text_list.extend(get_quotes())
        text_list.extend(get_funfacts())
        random.shuffle(text_list)
    return text_list


def get_quote_funfact(text_list: List[str]) -> str:
    """
    Utility to get random text from given list.
    """
    return random.choice(text_list)


def get_text_to_display() -> str:
    """
    Get text to display on readme, depending on option.
    """
    global OPTION
    text_list = get_option_list(OPTION)
    text_to_display = get_quote_funfact(text_list)
    text_to_display = re.sub('[\n]', '', text_to_display)
    text_to_display = re.sub('[\xa0]', ' ', text_to_display)
    text_to_display = f"<i>❝{text_to_display}❞</i>"
    return text_to_display


if __name__ == "__main__":
    text_to_display = get_text_to_display()
    print('text_to_display')
