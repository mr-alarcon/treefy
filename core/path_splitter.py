def split_path(urls):
    absolute_path = []
    relative_path = []

    for url in urls:
        if not url or url == "#":
            continue
        
        if url.startswith('http') or url.startswith('www.'):
            path = '/'.join(url.split('/')[3:])
            relative_path.append(path)
            absolute_path.append(url)

        else:
            relative_path.append(url)

    return absolute_path, relative_path

