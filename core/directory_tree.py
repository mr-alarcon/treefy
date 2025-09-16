"""
Module: directory_tree.py
Author: @mr-alarcon

Description:
    Provides functions to build a hierarchical directory like structure 
    from a list of URLs. Each URL is split into path segments, and these 
    segments are inserted into a nested dictionary that represents the 
    directory tree.

Functions:
    add_segments_to_tree(current_tree, segments):
        Inserts a list of segments into the current directory tree, 
        creating nested dictionaries for each missing segment.

    url_segments(url):
        Splits a URL into its path segments, ignoring fragment only links.

    create_directory_tree(links):
        Processes a list of URLs and builds a nested dictionary 
        that represents their hierarchical structure.
"""


def add_segments_to_tree(current_tree, segments):
    if not segments:
        return

    for segmt in segments:
        if segmt not in current_tree:
            current_tree[segmt] = {}

        current_tree = current_tree[segmt]
        

# Splits a URL into path segments, ignoring fragments (#).
def url_segments(url):
    if url.startswith("#"):
        return []
    else:
        url_seg = url.strip("/").split("/")
        return url_seg


# Creates a hierarchical tree from a list of URLs.
def create_directory_tree(links):
    directory_tree = {}

    for link in links:
        segments = url_segments(link)
        add_segments_to_tree(directory_tree, segments)

    return directory_tree


