def create_extensions_dict():
    exts = [
        "php", "asp", "aspx", "jsp", "cgi", "pl", "py", "rb",
        "js", "json", "xml",
        "env", "config", "ini", "yml", "yaml",
        "bak", "old", "zip", "rar",
        "log", "sql", "db",
        "htaccess", "htpasswd",
        "pem", "key", "crt", "p12", "pfx",
        "inc", "tpl", "sh", "exe", "bin", "ps1", "git",
        "html", "htm", "css",
        "jpg", "jpeg", "png", "gif", "svg", "webp", "ico",
        "woff", "woff2", "ttf", "eot",
        "mp4", "webm", "ogg", "mp3", "wav", "mov",
        "pdf", "doc", "docx", "xls", "xlsx", "ppt", "pptx"
    ]

    return exts



def create_categorize_extensios_dict():
    critical_exts = [
        "php", "asp", "aspx", "jsp", "cgi", "pl", "py", "rb",
        "sh", "exe", "bin", "ps1",
        "pem", "key", "crt", "p12", "pfx",
        "env", "config", "ini", "yml", "yaml",
        "htaccess", "htpasswd",
        "git",
        "inc", "tpl",
        "log", "sql", "db",
        "bak", "old", "zip", "rar"
    ]

    medium_exts = [
        "js", "json", "xml",
        "pdf", "doc", "docx", "xls", "xlsx", "ppt", "pptx"
    ]

    low_exts = [
        "html", "htm", "css",
        "jpg", "jpeg", "png", "gif", "svg", "webp", "ico",
        "woff", "woff2", "ttf", "eot",
        "mp4", "webm", "ogg", "mp3", "wav", "mov"
    ]

    return critical_exts, medium_exts, low_exts