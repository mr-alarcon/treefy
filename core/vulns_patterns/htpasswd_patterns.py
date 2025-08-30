vulns_patterns_htpasswd_dict = {

    "user_hash": [
        ":$apr1$",
        ":$2y$",
        ":$2a$",
        ":$2b$",
        ":$1$",
        ":{SHA}",
        ":{SSHA}"
    ],

    "credentials": [
        "admin",
        "root",
        "user",
        "test",
        "guest",
        "password",
        "123456",
        "qwerty"
    ],

    "misc_sensitive": [
        "htpasswd",
        "password",
        "login",
        "secret"
    ]
}
