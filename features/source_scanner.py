import requests

from patterns.hardcoded_patterns import HARDCODED_PATTERNS
from patterns.js_patterns import JS_PATTERNS

def source_scanner(files_urls):
    for url in files_urls:
        if url.endswith(".js"):
            response = requests.get(url, timeout=5)
            content_file = response.text

            for pattern_category, patterns in JS_PATTERNS.items():
                for pattern in patterns:
                    if pattern in content_file:
                        print(f"[+] Url file: {url}\n[+] Pattern category: {pattern_category}\n[+] Pattern found: {pattern}\n\n")
                    else:
                        pass

        