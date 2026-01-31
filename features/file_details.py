from urllib.parse import urlparse
from pathlib import Path
import os
import requests

from data.extension_category import EXTENSIONS_CATEGORY_INVERTED
from data.extension_risk import EXTENSIONS_RISK_INVERTED

files_details = []
    
def file_headers(file_url):
    try:
        response = requests.head(file_url, allow_redirects=True, timeout=10)
    except requests.RequestException:
        return "Unknown", "Unknown", "Unknown"

    size = response.headers.get("Content-Length")
    content_type = response.headers.get("Content-Type")
    last_modified = response.headers.get("Last-Modified")

    if size:
        size = int(size)
        for unit in ["B", "KB", "MB", "GB"]:
            if size < 1024:
                file_size = f"{size:.2f} {unit}"
                break
            size /= 1024
    else:
        file_size = "Unknown"

    file_type = content_type.split(";")[0] if content_type else "Unknown"
    last_modified = last_modified if last_modified else "Unknown"

    return file_size, file_type, last_modified


    
def file_details(files_urls):
    for url in files_urls:
        file_name = os.path.basename(urlparse(url).path)
        file_extension = Path(file_name).suffix.lower()
        extension_category = EXTENSIONS_CATEGORY_INVERTED.get(file_extension, "Unknown file type")
        extension_risk = EXTENSIONS_RISK_INVERTED.get(file_extension, "Unknown file type")
        file_size, file_type, file_last_modified = file_headers(url)

        files_details.append({
            "File name": file_name, 
            "File url": url, 
            "File size": file_size,
            "File type": file_type,
            "Last modified": file_last_modified,
            "File extension": file_extension, 
            "Extension category": extension_category,
            "Extension risk": extension_risk,
            })

    return files_details