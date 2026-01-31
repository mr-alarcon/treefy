EXTENSIONS_CATEGORY = {
    (".png", ".jpg", ".jpeg", ".gif", ".bmp", ".webp", ".svg", ".ico"): "Image file",
    (".mp4", ".avi", ".mkv", ".mov", ".webm", ".flv"): "Video file",
    (".mp3", ".wav", ".ogg", ".aac", ".flac", ".m4a"): "Audio file",
    (".pdf", ".doc", ".docx", ".xls", ".xlsx", ".ppt", ".pptx", ".txt"): "Document file",
    (".zip", ".rar", ".7z", ".tar", ".gz", ".bz2", ".xz", ".tgz"): "Compressed archive",
    (".html", ".htm", ".css", ".js", ".json", ".xml", ".map", ".wasm"): "Web file",
    (".py", ".c", ".cpp", ".h", ".java", ".go", ".rs", ".php", ".sh", ".ts", ".tsx", ".jsx", ".vue", ".cs", ".rb", ".pl"): "Source code file",
    (".exe", ".bin", ".app", ".run", ".elf", ".ps1", ".bat"): "Executable file",
    (".iso", ".img"): "Disk image",
    (".ttf", ".otf", ".woff", ".woff2", ".eot"): "Font file",
    (".conf", ".cfg", ".ini", ".yaml", ".yml", ".toml", ".env", ".env.example", ".properties", ".cnf", ".settings"): "Configuration file",
    (".sql", ".db", ".sqlite", ".sqlite3", ".mdb", ".accdb"): "Database file",
    (".bak", ".old", ".tmp", ".temp", ".swp", ".save", ".backup", ".bkp", ".orig"): "Backup/temporary file",
    (".log", ".trace", ".debug", ".dump", ".core"): "Log/dump file",
    (".pem", ".key", ".crt", ".csr", ".der", ".p12", ".pfx", ".jks", ".keystore"): "Security/certificate file",
    (".htaccess", ".htpasswd"): "Web security file"
}


EXTENSIONS_CATEGORY_INVERTED = {}

for exts, category in EXTENSIONS_CATEGORY.items():
    for ext in exts:
        EXTENSIONS_CATEGORY_INVERTED[ext] = category

    