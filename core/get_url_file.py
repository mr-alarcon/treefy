import os
from urllib.parse import urlparse

from core.extensions_files import create_extensions_dict

def get_url_files(absolute_urls):
    exts = create_extensions_dict()
    url_files = {}

    for url in absolute_urls:
        if url.lower().endswith(tuple(f".{ext}" for ext in exts)):
            path = urlparse(url).path
            filename = os.path.basename(path)
            clean_filename = filename.split("?")[0]

            url_files[clean_filename] = url

    return url_files
