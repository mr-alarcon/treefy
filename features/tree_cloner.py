from pathlib import Path
from urllib.parse import urlparse

def tree_cloner(tree_structure, url):
    parsed_url = urlparse(url).netloc
    parsed_url = parsed_url.replace(":", "_")

    root_directory = Path(f"./clones/{parsed_url}")
    root_directory.mkdir(parents=True, exist_ok=True)
