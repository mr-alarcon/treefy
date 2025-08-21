from pathlib import Path
import requests

from core.extensions_files import create_extensions_dict
from core.get_url_file import get_url_files


binary_requierd_exts = (
    "jpg", "jpeg", "png", "gif", "svg", "webp", "ico",
    "woff", "woff2", "ttf", "eot",
    "mp4", "webm", "ogg", "mp3", "wav", "mov",
    "zip", "rar",
    "exe", "bin",
    "pem", "key", "crt", "p12", "pfx",
    "pdf", "doc", "docx", "xls", "xlsx", "ppt", "pptx"
)

def create_local_clone_tree(absolute_urls, tree, base_path, get_urls_flag=True):
    global url_files
    
    exts = create_extensions_dict()

    if get_urls_flag:
        url_files = get_url_files(absolute_urls)

    for key, value in enumerate(tree.items()):
        is_file = key.split("?")[0].endswith(tuple(f".{ext}" for ext in exts))

        current_path = Path(base_path) / key.split("?")[0]

        if is_file:
            current_path.parent.mkdir(parents=True, exist_ok=True)
            
            if key in url_files:

                response = requests.get(url_files[key])

                if key.split("?")[0].endswith(binary_requierd_exts):
                    with current_path.open("wb") as file:
                        file.write(response.content)

                else:            
                    with current_path.open("w", encoding="utf-8") as file:
                        file.write(response.text)
                        file.close()
                        del file

        else:
            current_path.mkdir(parents=True, exist_ok=True)

        if isinstance(value, dict):
            create_local_clone_tree(absolute_urls, value, current_path, print_urls=False)
