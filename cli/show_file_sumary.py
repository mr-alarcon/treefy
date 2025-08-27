"""
Module: show_file_summary.py
Author: @mr-alarcon

Description:
    Provides a function to display a summary of files found in a website.
    The function groups files by type and prints the amount, category, and
    detailed list of file names in CLI.

Functions:
    show_file_sumary(urls):
        Prints a structured summary of all files retrieved from the given URLs.
"""

# Local modules imports
from core.path_splitter import split_path
from core.get_file_list import get_file_list

# Function to show the files sumary
def show_file_sumary(urls):
    # Get the relative URLs from the list of URLs
    _, relative_urls = split_path(urls)

    # Get a dictionary with information about the files grouped by type
    files_dict = get_file_list(relative_urls)

    # Iterates over each file type and its associated information
    for file_type, info_file in files_dict.items():
        print(f"[+] Type: {file_type}")

        for title_info, info in info_file.items():
            if title_info == "Amount" or title_info == "Category":
                print(f"[+] {title_info}: {info}")
            else:
                print(f"[+] {title_info}:")

                for i in info:
                    print(f"  • {i}")

        print("\n")