"""
Module: get_file_list.py
Author: @mr-alarcon

Description:
    Provides a function to process a list of URLs and identify files based 
    on their extensions. The function categorizes files into severity levels 
    (critical, medium, low, or unknown) depending on predefined extension groups. 
    For each extension found, it stores the total count and the list of filenames.

Functions:
    get_file_list(urls):
        Iterates through a list of URLs, extracts filenames, 
        matches them with known extensions, assigns a category 
        (critical/medium/low/unknown), and returns a dictionary 
        containing extension details, number of files, and filenames.
"""

# Standard library imports
import os
from urllib.parse import urlparse

# Local modules imports
from core.extensions_files import all_exts, critical_exts, medium_exts, low_exts

def get_file_list(urls):
    files_dict = {}
    
    # Iterate through all URLs provided
    for url in urls:
        path = urlparse(url).path
        filename = os.path.basename(path)
        clean_filename = filename.split("?")[0]
        
        # Check which extension the file belongs to
        for ext in all_exts:
            if clean_filename.lower().endswith(f".{ext}"):
                # Initialize dictionary entry for this extension if not exists
                files_dict.setdefault(ext, {"Category": "unknown", "Amount": 0, "Files": []})

                # Assign severity category depending on the extension
                if ext in critical_exts:
                    files_dict[ext]["Category"] = "critical"
                elif ext in medium_exts:
                    files_dict[ext]["Category"] = "medium"
                elif ext in low_exts:
                    files_dict[ext]["Category"] = "low"
                else:
                    files_dict[ext]["Category"] = "unknown"
                
                # Update counter and append filename
                files_dict[ext]["Amount"] += 1
                files_dict[ext]["Files"].append(clean_filename)
                break 

    return files_dict
