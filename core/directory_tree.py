def add_segments_to_tree(current_tree, segments):
    for segmt in segments:
        if segmt not in current_tree:
            current_tree[segmt] = {}

        current_tree = current_tree[segmt]


def url_segments(url):
    if url.startswith("#"):
        return
    else:
        url_seg = url.strip("/").split("/")
        return url_seg


def create_directory_tree(links):
    directory_tree = {}

    for link in links:
        segments = url_segments(link)
        add_segments_to_tree(directory_tree, segments)

    return directory_tree


