"""
This module provides functionality to verify whether a target website
is reachable and responds to HTTP requests before executing further
processing steps.
"""

import requests

def check_status_code(url):
    try:
        response = requests.head(url, timeout=5, allow_redirects=True)
        return response.status_code < 400, response.status_code
    
    except requests.exceptions.RequestException:
        return False, None
