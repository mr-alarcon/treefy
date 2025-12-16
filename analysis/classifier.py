"""
URL analysis utilities for classifying discovered URLs by type and domain.
"""

import os
from urllib.parse import urlparse

def get_base_url(url_target):
    parsed = urlparse(url_target)
    return f"{parsed.scheme}://{parsed.netloc}"


def get_domain(url):
    return urlparse(url).netloc.split(":")[0]


def derive_directories_from_files(file_urls):
    """
    Extract parent directory paths from file URLs,
    preserving the directory hierarchy.
    """
    derived_dirs = set()

    for url in file_urls:
        path = urlparse(url).path
        segments = path.strip("/").split("/")

        current = ""
        for segment in segments[:-1]:
            current += f"/{segment}"
            derived_dirs.add(current + "/")

    return derived_dirs


def classifier_urls(url_target, urls):
    """
    Classify URLs relative to a target domain into files, directories,
    subdomains and external domains.
    """
    files_urls = []
    directory_urls = []
    subdomains_urls = []
    external_domains_urls = []

    base_domain = get_domain(url_target)

    for url in urls:
        domain = get_domain(url)

        if domain == "" or domain == base_domain:
            path = urlparse(url).path
            _, ext = os.path.splitext(path)

            if ext:
                files_urls.append(url)
            else:
                directory_urls.append(url)

        elif domain.endswith("." + base_domain):
            subdomains_urls.append(url)
        else:
            external_domains_urls.append(url)

        
    base_url = get_base_url(url_target)

    derived_dirs = {
        base_url + d for d in derive_directories_from_files(files_urls)
    }

    directory_urls = sorted(set(directory_urls) | set(derived_dirs))
   
    return files_urls, directory_urls, subdomains_urls, external_domains_urls