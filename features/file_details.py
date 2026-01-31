from urllib.parse import urlparse
from pathlib import Path
import os

from data.extension_category import EXTENSIONS_CATEGORY_INVERTED

files_details = []

def file_details(files_urls):
    for url in files_urls:
        file_name = os.path.basename(urlparse(url).path)
        file_extension = Path(file_name).suffix.lower()
        extension_category = EXTENSIONS_CATEGORY_INVERTED.get(file_extension, "Unknown file type")
        files_details.append({"File name": file_name, "File url": url, "File extension": file_extension, "Extension category": extension_category})

    return files_details