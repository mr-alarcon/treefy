"""
Module: save_output_file.py
Author: @mr-alarcon

Description:
    Provides a function to redirect stdout so that all printed output is displayed 
    in the terminal and simultaneously saved into a file. ANSI escape codes 
    are stripped before being written to the file.

Functions:
    save_output_file(file_name):
        Redirects sys.stdout to write both to the terminal and the specified file,
        removing ANSI escape codes from the file output.
"""

# Standard library imports
import sys
import re

# Regex pattern to detect and remove ANSI escape codes
ANSI_ESCAPE = re.compile(r'\x1B\[[0-?]*[ -/]*[@-~]')

 # Open the output file in write mode
def save_output_file(file_name):
    file = open(file_name, "w", encoding="utf-8")
    stdout_original = sys.__stdout__

    def write(data):
        # Write raw output to the terminal
        stdout_original.write(data)           

        # Remove ANSI escape codes before writing to the file  
        clean_data = ANSI_ESCAPE.sub('', data)
        file.write(clean_data)                    

    # Ensure both terminal and file buffers are flushed
    def flush():
        stdout_original.flush()
        file.flush()

    # Override sys.stdout methods to use our custom behavior
    sys.stdout.write = write
    sys.stdout.flush = flush

    