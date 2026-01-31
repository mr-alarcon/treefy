import sys
import re
from types import SimpleNamespace

ANSI_ESCAPE = re.compile(r'\x1B\[[0-?]*[ -/]*[@-~]')

_REAL_STDOUT = sys.__stdout__ 

def save_output_file(file_path):
    file = open(f"{file_path}", "w", encoding="utf-8")

    def write(data):
        _REAL_STDOUT.write(data)
        clean = ANSI_ESCAPE.sub("", data)
        file.write(clean)

    def flush():
        _REAL_STDOUT.flush()
        file.flush()

    def close():
        flush()
        file.close()
        sys.stdout = _REAL_STDOUT

    sys.stdout = SimpleNamespace(
        write=write,
        flush=flush,
        close=close
    )
