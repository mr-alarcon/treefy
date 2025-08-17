import time
from colorama import Fore as F
from colorama import init

from core.extensions_files import create_extensions_dict

init(autoreset=True)

def show_tree(tree, icon_type=1, level=0, prefix=""):
    global color, icon

    exts = create_extensions_dict()

    keys = list(tree.keys())

    for i, (key, value) in enumerate(tree.items()):
        is_file = key.split("?")[0].endswith(tuple(f".{ext}" for ext in exts))
        is_last = (i == len(keys) - 1)

        color = F.RED if is_file else F.GREEN

        if icon_type == 1:
            icon = "📄" if is_file else "📁"
        else:
            icon = "+" if is_file else "\\"

        connector = "└──" if is_last else "├──"

        time.sleep(0.1)
        print(f"{prefix}{F.YELLOW}{connector} {color}{icon} {key}")

        if isinstance(value, dict):
            new_prefix = prefix + ("    " if is_last else f"{F.YELLOW}│   ")
            show_tree(value, icon_type, level + 1, new_prefix)

