"""
This module coordinates the main execution flow of the application
"""

from core.target_status import check_status_code
from discovery.urls import extract_urls, filter_urls, normalize_urls, deduplicate_urls

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

    print(len(urls_found))
    print(len(urls_filtered))
    print(len(urls_normalized))
    print(len(urls_deduplicated))
    

    