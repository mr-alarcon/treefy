from pathlib import Path

from core.extensions_files import create_extensions_dict
from core.get_url_file import get_url_files

def create_local_clone_tree(absolute_urls, tree, base_path, print_urls=True):
    exts = create_extensions_dict()

    if print_urls:
        url_files = get_url_files(absolute_urls)
        
    for i, (key, value) in enumerate(tree.items()):
        is_file = key.split("?")[0].endswith(tuple(f".{ext}" for ext in exts))

        current_path = Path(base_path) / key.split("?")[0]

        if is_file:
            current_path.parent.mkdir(parents=True, exist_ok=True)
            current_path.touch(exist_ok=True) 
        else:
            current_path.mkdir(parents=True, exist_ok=True)

        if isinstance(value, dict):
            create_local_clone_tree(absolute_urls, value, current_path, print_urls=False)
