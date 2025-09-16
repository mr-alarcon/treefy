"""
Module: local_clone_tree.py
Author: @mr-alarcon

Description:
    Provides a function to create a local clone of a website's directory structure.
    It recursively traverses the list of URLs or directory tree, creates corresponding
    folders and files on the local filesystem, and saves file contents in text or
    binary mode depending on the file extension.

Functions:
    create_local_clone_tree(urls_list, destination_path, initial_call=True):
        Recursively builds the local directory structure and downloads files from
        the provided URLs.
"""


# Standard library imports
from pathlib import Path
import requests

# Local modules imports
from core.extensions_files import all_exts, binary_exts
from core.get_url_file import get_url_files
from core.path_splitter import split_path
from core.directory_tree import create_directory_tree


# Function to create a local directory tree clone 
def create_local_clone_tree(urls_list, destination_path, initial_call=True, url_base=None):
    global base, url_files

    # Use `initial_call` to run this block only on the first function call
    if initial_call:
        absolute_urls, relative_urls = split_path(urls_list)
        url_files = get_url_files(relative_urls)
        base = url_base
        directory_tree = create_directory_tree(relative_urls)
    else:
        directory_tree = urls_list

    for item_name, item_content in directory_tree.items():
        # Identify if is a file
        file_flag = item_name.split("?")[0].endswith(tuple(f".{ext}" for ext in all_exts))

        # Create the full path where the file or folder will be saved
        current_path = Path(destination_path) / item_name.split("?")[0]

        # If the item is a file create the parents directories
        if file_flag:
            current_path.parent.mkdir(parents=True, exist_ok=True)
            
            if item_name in url_files:

                response = requests.get(base, url_files[item_name])

                # Save file in binary mode
                if item_name.split("?")[0].endswith(binary_exts):
                    with current_path.open("wb") as file:
                        file.write(response.content)

                # Save file in text mode
                else:            
                    with current_path.open("w", encoding="utf-8") as file:
                        file.write(response.text)

        # If the item is a directory, create the folder
        else:
            current_path.mkdir(parents=True, exist_ok=True)

        # If the current item is a directory, execute the function recursively
        if isinstance(item_content, dict):
            create_local_clone_tree(item_content, current_path, initial_call=False)
