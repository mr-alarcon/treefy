"""
Utilities for building a directory tree from URLs.

This module creates a nested dictionary representing
directories and files based on parsed URL paths.
"""

from urllib.parse import urlparse

def tree_builder(directory_urls):
    """
    Build a nested directory tree from directory URLs.
    """
        
    tree = {}

    for directory in directory_urls:
        current = tree

        path = urlparse(directory).path
        path_segments = [seg for seg in path.split("/") if seg]

        for segment in path_segments:
            if segment not in current:
                current[segment] = {}

            current = current[segment]

    return tree


            
def add_files_to_tree(tree, files_urls):
    """
    Insert file paths into an existing directory tree.
    """

    for file_url in files_urls:
        current = tree

        path = urlparse(file_url).path
        segments = [seg for seg in path.split("/") if seg]

        *dirs, filename = segments

        for segment in dirs:
            current = current.setdefault(segment, {})

        if filename not in current:
            current[filename] = None

    return tree