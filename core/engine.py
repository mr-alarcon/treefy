"""
This module coordinates the main execution flow of the application
"""

from core.target_status import check_status_code

def run(url, tree):
    status, code = check_status_code(url)

    if status:
        print(f"[+] Target accessible ({code})")
    else:
        print(f"[!] Target not accessible ({code})")


    