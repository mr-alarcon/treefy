from urllib.parse import urlparse
import os

files_details = []

def file_details(files_urls):
    for url in files_urls:
        file_name = os.path.basename(urlparse(url).path)
        files_details.append({"File name": file_name, "File url": url})

    return files_details