"""
This module is responsible for retrieving a target web page and
extracting all URLs found in common HTML elements
"""

import requests 
from bs4 import BeautifulSoup
from urllib.parse import unquote, urljoin

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



def filter_urls(urls_found):
    urls_filtered = []

    for url in urls_found:
        if url.startswith(("#", "tel:", "mailto:", "javascript:")):
            continue
        else:
            urls_filtered.append(url)

    urls_filtered = list(set(urls_filtered))

    return urls_filtered



def normalize_urls(url_target, urls_filtered):
    urls_normalized = []

    for url in urls_filtered:
        url = urljoin(url_target, url)
        urls_normalized.append(url)

    return urls_normalized
