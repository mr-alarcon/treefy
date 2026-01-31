EXTENSIONS_RISK = {
    (".png", ".jpg", ".jpeg", ".gif", ".bmp", ".webp", ".svg", ".ico",
     ".mp4", ".avi", ".mkv", ".mov", ".webm", ".flv",
     ".mp3", ".wav", ".ogg", ".aac", ".flac", ".m4a",
     ".ttf", ".otf", ".woff", ".woff2", ".eot"): "Low",

    (".html", ".htm", ".css", ".js", ".json", ".xml", ".map", ".wasm",
     ".pdf", ".txt",
     ".log", ".trace", ".debug"): "Medium",
     
    (".zip", ".rar", ".7z", ".tar", ".gz", ".bz2", ".xz", ".tgz",
     ".bak", ".old", ".tmp", ".temp", ".swp", ".save", ".backup", ".bkp", ".orig",
     ".sql", ".db", ".sqlite", ".sqlite3", ".mdb", ".accdb",
     ".conf", ".cfg", ".ini", ".yaml", ".yml", ".toml", ".env", ".env.example",
     ".properties", ".cnf", ".settings"): "High",

    (".pem", ".key", ".crt", ".csr", ".der", ".p12", ".pfx", ".jks", ".keystore",
     ".htaccess", ".htpasswd",
     ".exe", ".bin", ".app", ".run", ".elf", ".ps1", ".bat",
     ".py", ".c", ".cpp", ".h", ".java", ".go", ".rs", ".php", ".sh",
     ".ts", ".tsx", ".jsx", ".vue", ".cs", ".rb", ".pl"): "Critical"
}


EXTENSIONS_RISK_INVERTED = {}

for exts, risk in EXTENSIONS_RISK.items():
    for ext in exts:
        EXTENSIONS_RISK_INVERTED[ext] = risk
