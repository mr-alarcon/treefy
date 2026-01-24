from pathlib import Path
from urllib.parse import urlparse

def create_base_path(url):
    parsed_url = urlparse(url).netloc
    parsed_url = parsed_url.replace(":", "_")

    base_path = Path(f"./clones/{parsed_url}")
    base_path.mkdir(parents=True, exist_ok=True)

    return base_path


def tree_cloner(tree_strucutre, base_path):
    for name, content in tree_strucutre.items():
        safe_name = Path(name).name
        path = base_path / safe_name

        if content is None:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.touch(exist_ok=True)            
        elif isinstance(content, dict):
            path.mkdir(parents=True, exist_ok=True)
            tree_cloner(content, path)
