"""
This module coordinates the main execution flow of the application
"""

from core.target_status import check_status_code
from discovery.urls import extract_urls, filter_urls

def run(url, tree):
    status, code = check_status_code(url)

    if status:
        print(f"[+] Target accessible ({code})")
    else:
        print(f"[!] Target not accessible ({code})")
        return 
    
    urls_found = extract_urls(url)
    print(len(urls_found))

    urls_found = filter_urls(urls_found)
    print(len(urls_found))


    