"""
Module: show_tree.py
Author: @mr-alarcon

Description:
    Provides a function to create and display a visual directory tree
    of website URLs in the CLI, with optional emojis and colors.
    
Functions:
    show_tree(url_list, use_emojis=True, level=0, tree_prefix="", initial_call=True):
        Recursively prints the directory structure of URLs.
"""

# Standard library imports
from colorama import Fore as F
from colorama import init

# Local modules imports
from core.extensions_files import all_exts
from core.path_splitter import split_path
from core.directory_tree import create_directory_tree

init(autoreset=True)

# Function to create a directory tree and show it
def show_tree(urls_list, emojis, level=0, tree_prefix="", initial_call=True):

    # Use `initial_call` to run this block only on the first function call
    if initial_call:
        _, relative_urls = split_path(urls_list)
        directory_tree = create_directory_tree(relative_urls)
    else:
        directory_tree = urls_list

    keys = list(directory_tree.keys())
    
    for i, (item_name, item_content) in enumerate(directory_tree.items()):
        # Identify if is a file
        file_flag = item_name.split("?")[0].endswith(tuple(f".{ext}" for ext in all_exts))

        # Check if this is the last item in the current directory
        last_item_flag = (i == len(keys) - 1)
        
        # Adjust colors, tree connectors, and icons based on file or folder type
        color = F.RED if file_flag else F.GREEN
        connector = "└──" if last_item_flag else "├──" 

        if emojis:
            icon = "📄" if file_flag else "📁"
        else:
            icon = "+" if file_flag else "\\"

        print(f"{tree_prefix}{F.YELLOW}{connector} {color}{icon} {item_name}")

        # If the current item is a directory, execute the function recursively
        if isinstance(item_content, dict):
            new_prefix = tree_prefix + ("    " if last_item_flag else f"{F.YELLOW}│   ")
            show_tree(item_content, emojis, level + 1, new_prefix, initial_call=False)

