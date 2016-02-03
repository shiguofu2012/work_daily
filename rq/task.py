#!/usr/bin/python

import requests
import time


def count_words(url):
    resp = requests.get(url)
    time.sleep(5)
    return len(resp.text.split())
