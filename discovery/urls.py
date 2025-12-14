"""
This module is responsible for retrieving a target web page and
extracting all URLs found in common HTML elements
"""

import requests 
from bs4 import BeautifulSoup
from urllib.parse import unquote

def extract_urls(url_target):
    urls_found = []

    response = requests.get(url_target)
    source_code = BeautifulSoup(response.text, "html.parser")

    href_tags = source_code.find_all(["a", "img", "script", "link"], href=True)
    src_tags = source_code.find_all(["img", "script", "iframe"], src=True)

    for tag in href_tags:
        raw_url = tag["href"]
        clean_url = unquote(raw_url).strip().replace(",", "")
        urls_found.append(clean_url)

    for tag in src_tags:
        raw_url = tag["src"]
        clean_url = unquote(raw_url).strip().replace(",", "")
        urls_found.append(clean_url)

    return urls_found