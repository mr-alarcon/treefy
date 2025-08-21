import sys

def save_output_file(filename, mode="w"):
    file = open(filename, mode, encoding="utf-8")
    stdout_original = sys.stdout

    def write(data):
        stdout_original.write(data) 
        file.write(data)         

    def flush():
        stdout_original.flush()
        file.flush()

    sys.stdout.write = write
    sys.stdout.flush = flush
    return file 
