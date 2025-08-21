import requests

from core.get_url_file import get_url_files
from core.vuln_patterns import create_vulns_patterns_js

binary_requierd_exts = (
    "jpg", "jpeg", "png", "gif", "svg", "webp", "ico",
    "woff", "woff2", "ttf", "eot",
    "mp4", "webm", "ogg", "mp3", "wav", "mov",
    "zip", "rar",
    "exe", "bin",
    "pem", "key", "crt", "p12", "pfx",
    "pdf", "doc", "docx", "xls", "xlsx", "ppt", "pptx"
)


def scan_files(absolute_urls):
    global url_files

    vulns_patterns_js = create_vulns_patterns_js()

    url_files = get_url_files(absolute_urls)

    for key, value in url_files.items():

        if key.split("?")[0].endswith(binary_requierd_exts):
            continue
        else:
            response = requests.get(value)

            for vulns_name, vulns_payload in vulns_patterns_js.items():
                for vuln in vulns_payload:
                    if vuln in response.text:
                        print(f"[!] Dectect {vulns_name} in {key} file")