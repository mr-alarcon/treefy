"""
Module: get_url_files.py
Author: @mr-alarcon

Description:
    Provides a function to filter and map URLs that reference files. 
    It checks whether a URL ends with a known file extension, extracts 
    the filename, and creates a dictionary mapping each filename to its 
    absolute URL.

Functions:
    get_url_files(absolute_urls):
        Iterates over a list of absolute URLs, selects those that match 
        known file extensions, cleans the filename, and stores them in 
        a dictionary {filename: url}. 
        Returns the dictionary of matching files.
"""

# Standard library imports
import os
from urllib.parse import urlparse

# Local modules imports
from core.extensions_files import all_exts

def get_url_files(absolute_urls):
    url_files = {}

    # Iterate through all provided URLs
    for url in absolute_urls:
        if url.lower().split("?")[0].endswith(tuple(f".{ext}" for ext in all_exts)):
            path = urlparse(url).path
            file_name = os.path.basename(path)
            clean_filename = file_name.split("?")[0]

            url_files[clean_filename] = url
            
    # Return dictionary {filename: url}
    return url_files
