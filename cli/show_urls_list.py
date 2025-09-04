"""
Module: show_urls_list.py
Author: @mr-alarcon

Description:
    Provides a function to display the full URLs found in a website
    in the CLI. It converts relative URLs to absolute URLs using the 
    given base URL.

Functions:
    show_urls_list(urls, base_url):
        Prints each URL in the CLI after joining it with the base URL.
"""

# Standard library imports
from urllib.parse import urljoin
from colorama import Fore as F

# Local modules imports
from core.path_splitter import split_path

# Function to display the list of URLs in the CLI
def show_urls_list(urls, base_url):
    # Get the relative URLs from the list of URLs
    _, relative_urls = split_path(urls)

    # Prepend the base URL to each relative URL to get the full link
    for url in list(set(relative_urls)):
        full_url = urljoin(base_url + "/", url)
        print(f"{F.GREEN}[+] {F.WHITE}{full_url}{F.RESET}")
