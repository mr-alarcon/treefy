import requests

from core.get_url_file import get_url_files


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

    url_files = get_url_files(absolute_urls)

    for key, value in url_files.items():

        if key.split("?")[0].endswith(binary_requierd_exts):
            continue
        else:
            response = requests.get(value)

            if "gffdsing" in response.text:
                pass
            else:
                pass