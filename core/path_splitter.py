"""
Module: local_clone_tree.py
Author: @mr-alarcon

Description:
    Provides functions to handle URL paths. 
    Currently splits a list of URLs into absolute URLs and relative paths.

Functions:
    split_path(urls):
        Returns two lists: absolute_path and relative_path.
"""


def split_path(urls):
    # Initialize lists to store absolute and relative paths
    absolute_path = []
    relative_path = []

    for url in urls:
        # Skip empty values or placeholders like "#"
        if not url or url == "#":
            continue
        
         # If the string looks like a full URL (absolute path)
        if url.startswith('http') or url.startswith('www.'):
            path = '/'.join(url.split('/')[3:])
            relative_path.append(path)
            absolute_path.append(url)
            
        # Otherwise, treat it as a relative path directly
        else:
            relative_path.append(url)

    return absolute_path, relative_path
