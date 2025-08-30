vulns_patterns_git_dict = {

    "credentials": [
        "password",
        "passwd",
        "secret",
        "api_key",
        "token",
        "access_key",
        "private_key",
        "db_password",
        "db_user"
    ],

    "endpoints_http": [
        "http://",
        "url",
        "endpoint"
    ],

    "endpoints_https": [
        "https://",
        "url",
        "endpoint"
    ],

    "misc_sensitive": [
        "config",
        "env",
        "debug",
        "key",
        "certificate",
        "client_secret"
    ],

    "git_sensitive": [
        ".git/config",
        ".git/credentials",
        "refs/remotes/origin",
        "HEAD"
    ]
}
