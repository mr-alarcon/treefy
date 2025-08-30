vulns_patterns_key_dict = {

    "private_keys": [
        "-----BEGIN PRIVATE KEY-----",
        "-----BEGIN RSA PRIVATE KEY-----",
        "-----BEGIN DSA PRIVATE KEY-----",
        "-----BEGIN EC PRIVATE KEY-----",
        "-----BEGIN ENCRYPTED PRIVATE KEY-----"
    ],

    "api_keys": [
        "api_key=",
        "API_KEY=",
        "key=",
        "KEY=",
        "access_key=",
        "private_key="
    ],

    "misc_sensitive": [
        "token",
        "secret",
        "auth",
        "credential"
    ]
}
