"""
Module: extensions_files.py
Author: @mr-alarcon

Description:
    Defines lists and categories of file extensions used to classify 
    resources extracted from URLs. Extensions are grouped by risk level 
    (critical, medium, low). This module provides a reference for filtering, 
    categorizing, and analyzing files based on their extensions.

Variables:
    all_exts (list): Comprehensive list of supported file extensions.
    binary_exts (tuple): Extensions that represent binary files 
                         (e.g., images, videos, executables, archives).
    critical_exts (list): Extensions considered high-risk (e.g., config, 
                          credentials, server-side scripts, backups).
    medium_exts (list): Extensions considered moderate-risk 
                        (e.g., documents, scripts, structured data).
    low_exts (list): Extensions considered low-risk (e.g., static content 
                     like HTML, CSS, images, fonts, and media).
"""

all_exts = [
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

binary_exts = (
    "jpg", "jpeg", "png", "gif", "svg", "webp", "ico",
    "woff", "woff2", "ttf", "eot",
    "mp4", "webm", "ogg", "mp3", "wav", "mov",
    "zip", "rar",
    "exe", "bin",
    "pem", "key", "crt", "p12", "pfx",
    "pdf", "doc", "docx", "xls", "xlsx", "ppt", "pptx"
)

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