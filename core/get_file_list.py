import os
from urllib.parse import urlparse

from core.extensions_files import create_extensions_dict, create_categorize_extensios_dict

def get_file_list(urls):
    files_dict = {}
    exts = create_extensions_dict()
    critical_exts, medium_exts, low_exts = create_categorize_extensios_dict()
    
    for url in urls:
        path = urlparse(url).path
        filename = os.path.basename(path)
        clean_filename = filename.split("?")[0]
        
        for ext in exts:
            if clean_filename.lower().endswith(f".{ext}"):
                files_dict.setdefault(ext, {"Category": "unknown", "Amount": 0, "Files": []})

                if ext in critical_exts:
                    files_dict[ext]["Category"] = "critical"
                elif ext in medium_exts:
                    files_dict[ext]["Category"] = "medium"
                elif ext in low_exts:
                    files_dict[ext]["Category"] = "low"
                else:
                    files_dict[ext]["Category"] = "unknown"

                files_dict[ext]["Amount"] += 1
                files_dict[ext]["Files"].append(clean_filename)
                break 

    return files_dict
