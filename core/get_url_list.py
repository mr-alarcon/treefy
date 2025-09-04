"""
Module: get_url_list.py
Author: @mr-alarcon

Description:
    Provides a function to extract all URLs from a given webpage. 
    It parses HTML content and collects values from 'href' and 'src' 
    attributes in tags like <a>, <img>, <script>, <link>, and <iframe>. 
    Optionally, SSL certificate verification can be enabled or disabled 
    when making the request.

Functions:
    get_url_list(url, ssl_certified=False):
        Sends an HTTP request to the target URL, retrieves the page content, 
        and extracts/cleans all href/src values found. 
        Returns a list of URLs or None if the request fails.
"""

# Standard library imports
import requests
from bs4 import BeautifulSoup
import urllib3
from urllib.parse import unquote


# Disable SSL warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def get_url_list(url, ssl_certified=False):
    urls_found = []

    if ssl_certified:
        response = requests.get(url, allow_redirects=False)

    else:
        response = requests.get(url, verify=False, allow_redirects=False)
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    # Only process page if request was successful
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")

         # Collect tags that may contain links
        tags_with_href = soup.find_all(["a", "img", "script", "link"], href=True)
        tags_with_src  = soup.find_all(["img", "script", "iframe"], src=True)

        # Extract and clean URLs from "href" attributes
        for tag in tags_with_href:
            raw_url = tag["href"]
            clean_url = unquote(raw_url).strip().replace(",", "")
            urls_found.append(clean_url)

        # Extract and clean URLs from "src" attributes
        for tag in tags_with_src:
            raw_url = tag["src"]
            clean_url = unquote(raw_url).strip().replace(",", "")
            urls_found.append(clean_url)

    # If request fails, return None        
    else:
        return

    return list(set(urls_found))
