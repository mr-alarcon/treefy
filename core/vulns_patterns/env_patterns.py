vulns_patterns_env_dict = {

    "credentials": [
        "PASSWORD=",
        "PASS=",
        "SECRET=",
        "API_KEY=",
        "TOKEN=",
        "ACCESS_KEY=",
        "PRIVATE_KEY=",
        "DB_PASSWORD=",
        "DB_USER="
    ],

    "endpoints_http": [
        "http://",
        "URL=",
        "ENDPOINT="
    ],

    "endpoints_https": [
        "https://",
        "URL=",
        "ENDPOINT="
    ],

    "auth_tokens": [
        "BEARER=",
        "JWT=",
        "AUTH_TOKEN=",
        "SESSION_TOKEN="
    ],

    "database_configs": [
        "HOST=",
        "DB=",
        "DATABASE=",
        "USERNAME=",
        "USER=",
        "PORT="
    ],

    "misc_sensitive": [
        "CONFIG=",
        "ENV=",
        "DEBUG=",
        "KEY=",
        "CERTIFICATE=",
        "CLIENT_SECRET="
    ]
}
