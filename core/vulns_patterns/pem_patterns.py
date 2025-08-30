vulns_patterns_pem_dict = {

    "private_keys": [
        "-----BEGIN PRIVATE KEY-----",
        "-----BEGIN RSA PRIVATE KEY-----",
        "-----BEGIN DSA PRIVATE KEY-----",
        "-----BEGIN EC PRIVATE KEY-----",
        "-----BEGIN ENCRYPTED PRIVATE KEY-----"
    ],

    "certificates": [
        "-----BEGIN CERTIFICATE-----",
        "-----BEGIN CERTIFICATE REQUEST-----",
        "-----BEGIN PUBLIC KEY-----"
    ],

    "misc_sensitive": [
        "key",
        "cert",
        "certificate",
        "ssl",
        "tls"
    ]
}
