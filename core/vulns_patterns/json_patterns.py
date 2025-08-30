vulns_patterns_json_dict = {

    "credentials": [
        "\"password\"",
        "\"passwd\"",
        "\"secret\"",
        "\"api_key\"",
        "\"token\"",
        "\"access_key\"",
        "\"private_key\""
    ],

    "endpoints_http": [
        "\"http://",
        "\"url\": \"http://",
        "\"endpoint\": \"http://"
    ],

    "endpoints_https": [
        "\"https://",
        "\"url\": \"https://",
        "\"endpoint\": \"https://"
    ],

    "auth_tokens": [
        "\"bearer\"",
        "\"jwt\"",
        "\"auth_token\"",
        "\"session_token\""
    ],

    "database_configs": [
        "\"host\"",
        "\"db\"",
        "\"database\"",
        "\"username\"",
        "\"user\"",
        "\"port\""
    ],

    "misc_sensitive": [
        "\"config\"",
        "\"env\"",
        "\"debug\"",
        "\"key\"",
        "\"certificate\"",
        "\"client_secret\""
    ]
}
