import sys
import re

ANSI_ESCAPE = re.compile(r'\x1B\[[0-?]*[ -/]*[@-~]')

def save_output_file(file_name):
    file = open(file_name, "w", encoding="utf-8")
    stdout_original = sys.__stdout__

    def write(data):
        stdout_original.write(data)             
        clean_data = ANSI_ESCAPE.sub('', data)
        file.write(clean_data)                    

    def flush():
        stdout_original.flush()
        file.flush()

    sys.stdout.write = write
    sys.stdout.flush = flush

    