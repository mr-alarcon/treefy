def print_tree(tree, emojis, prefix=""):
    """
    Utilities for printing a directory tree to the terminal
    """
    if not isinstance(tree, dict):
        return  
    
    items = list(tree.items())
    total = len(items)

    if emojis:
        file_icon = "📄"
        dir_icon = "📁"
    else:
        file_icon = ""
        dir_icon = ""

    for index, (name, node) in enumerate(items):
        is_last = index == total - 1
        connector = f"└── " if is_last else f"├── "

        if isinstance(node, str):
            print(prefix + connector + file_icon + name)

        elif isinstance(node, dict):
            print(prefix + connector + dir_icon + name + "/")
            extension = "    " if is_last else "│   "
            print_tree(node, emojis, prefix + extension)
