"""
URL analysis utilities for classifying discovered URLs by type and domain.
"""

import os
from urllib.parse import urlparse

def get_domain(url):
    return urlparse(url).netloc.split(":")[0]


def classifier_urls(url_target, urls):
    """
    Classify URLs relative to a target domain into files, directories,
    subdomains and external domains.
    """
    files_urls = []
    directory_url = []
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
                directory_url.append(url)

        elif domain.endswith("." + base_domain):
            subdomains_urls.append(url)
        else:
            external_domains_urls.append(url)
   
    return files_urls, directory_url, subdomains_urls, external_domains_urls