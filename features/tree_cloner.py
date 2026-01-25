from pathlib import Path
from urllib.parse import urlparse
import requests

def create_base_path(url, root_path):
    parsed_url = urlparse(url).netloc
    parsed_url = parsed_url.replace(":", "_")

    if root_path.endswith("/"):
        pass
    else:
        root_path = root_path + "/"
        
    base_path = Path(f"{root_path}{parsed_url}")
    base_path.mkdir(parents=True, exist_ok=True)

    return base_path



def tree_cloner(tree_structure, base_path):
    for name, content in tree_structure.items():
        safe_name = Path(name).name
        path = base_path / safe_name

        if isinstance(content, dict):
            path.mkdir(parents=True, exist_ok=True)
            tree_cloner(content, path)

        elif isinstance(content, str):
            path.parent.mkdir(parents=True, exist_ok=True)

            try:
                response = requests.get(content, timeout=10)
                response.raise_for_status()
                path.write_bytes(response.content)
            except Exception as e:
                continue
