from pathlib import Path

from core.extensions_files import create_extensions_dict

def create_local_clone_tree(tree, base_path):
    exts = create_extensions_dict()

    for i, (key, value) in enumerate(tree.items()):
        is_file = key.split("?")[0].endswith(tuple(f".{ext}" for ext in exts))

        current_path = Path(base_path) / key.split("?")[0]

        if is_file:
            current_path.parent.mkdir(parents=True, exist_ok=True)
            current_path.touch(exist_ok=True) 
        else:
            current_path.mkdir(parents=True, exist_ok=True)

        if isinstance(value, dict):
            create_local_clone_tree(value, current_path)