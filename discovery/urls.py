"""
This module is responsible for retrieving a target web page and
extracting all URLs found in common HTML elements
"""

import requests 
from bs4 import BeautifulSoup
from urllib.parse import unquote, urljoin, urlparse, urlunparse


def extract_urls(url_target):
    """
    Retrieve the target page and extract raw URLs from common HTML elements.
    """
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
    """
    Remove non navigable URLs such as anchors and unsupported schemes.
    """
    urls_filtered = []

    for url in urls_found:
        if url.startswith(("#", "tel:", "mailto:", "javascript:")):
            continue
        else:
            urls_filtered.append(url)

    return urls_filtered



def normalize_urls(url_target, urls_filtered):
    """
    Normalize URLs by resolving relative and protocol relative paths
    using the target URL as base.
    """
    urls_normalized = []

    for url in urls_filtered:
        url_absolute = urljoin(url_target, url)
        
        url_parsed = urlparse(url_absolute)
        url_normalized = urlunparse(url_parsed._replace(query="", fragment=""))

        urls_normalized.append(url_normalized)

    return urls_normalized



def deduplicate_urls(urls_normalized):
    """
    Remove duplicate URLs while preserving their original order.
    """
    urls_deduplicated = []
    seen = set()
    
    for url in urls_normalized:
        if url not in seen:
            seen.add(url)
            urls_deduplicated.append(url)

    return urls_deduplicated
