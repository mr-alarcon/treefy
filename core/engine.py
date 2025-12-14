"""
This module coordinates the main execution flow of the application
"""

from core.target_status import check_status_code
from discovery.urls import extract_urls, filter_urls, normalize_urls, deduplicate_urls
from analysis.classifier import classifier_urls

def run(url, tree):
    status, code = check_status_code(url)

    if status:
        print(f"[+] Target accessible ({code})")
    else:
        print(f"[!] Target not accessible ({code})")
        return 
    
    urls_found = extract_urls(url)
    urls_filtered = filter_urls(urls_found)
    urls_normalized = normalize_urls(url, urls_filtered)
    urls_deduplicated = deduplicate_urls(urls_normalized)

    files_urls, directory_url, subdomains_urls, external_domains_urls = classifier_urls(url, urls_deduplicated)

    print(f"Total urls: {len(urls_deduplicated)}")
    print(f"Files urls: {len(files_urls)}")
    print(f"Directory urls: {len(directory_url)}")
    print(f"Subdomain urls: {len(subdomains_urls)}")
    print(f"External urls: {len(external_domains_urls)}")

    for i in urls_deduplicated:
        print(i)




    