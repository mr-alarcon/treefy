def matches_details_filters(file_info, details_name, details_ext, details_risk):
    if details_name:
        if details_name.lower() not in file_info["File name"].lower():
            return False

    if details_ext:
        ext = details_ext.lower()
        if not ext.startswith("."):
            ext = f".{ext}"
        if file_info["File extension"] != ext:
            return False

    if details_risk:
        if file_info["Extension risk"].lower() != details_risk.lower():
            return False

    return True
