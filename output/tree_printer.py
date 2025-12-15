def print_tree(tree, prefix=""):
    """
    Utilities for printing a directory tree to the terminal
    """
    items = list(tree.items())
    total = len(items)

    for index, (name, node) in enumerate(items):
        is_last = index == total - 1
        connector = "└── " if is_last else "├── "

        if node is None:
            print(prefix + connector + name)
        else:
            print(prefix + connector + name + "/")
            extension = "    " if is_last else "│   "
            print_tree(node, prefix + extension)
