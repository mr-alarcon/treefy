vulns_patterns_yaml_dict = {

    "credentials": [
        "password:",
        "passwd:",
        "secret:",
        "api_key:",
        "token:",
        "access_key:",
        "private_key:",
        "db_password:",
        "db_user:"
    ],

    "endpoints_http": [
        "http://",
        "url:",
        "endpoint:"
    ],

    "endpoints_https": [
        "https://",
        "url:",
        "endpoint:"
    ],

    "auth_tokens": [
        "bearer:",
        "jwt:",
        "auth_token:",
        "session_token:"
    ],

    "database_configs": [
        "host:",
        "db:",
        "database:",
        "username:",
        "user:",
        "port:"
    ],

    "misc_sensitive": [
        "config:",
        "env:",
        "debug:",
        "key:",
        "certificate:",
        "client_secret:"
    ]
}
