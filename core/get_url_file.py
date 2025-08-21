import os
from urllib.parse import urlparse

from core.extensions_files import create_extensions_dict

def get_url_files(absolute_urls):
    exts = create_extensions_dict()
    url_files = {}


    for url in absolute_urls:
        if url.lower().split("?")[0].endswith(tuple(f".{ext}" for ext in exts)):
            path = urlparse(url).path
            file_name = os.path.basename(path)
            clean_filename = file_name.split("?")[0]

            url_files[clean_filename] = url

    return url_files
