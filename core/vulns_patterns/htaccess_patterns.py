vulns_patterns_htaccess_dict = {

    "auth_basic": [
        "AuthType Basic",
        "AuthName",
        "AuthUserFile",
        "AuthGroupFile",
        "Require valid-user"
    ],

    "password_files": [
        ".htpasswd",
        "htpasswd"
    ],

    "redirects": [
        "Redirect ",
        "RedirectMatch ",
        "RewriteRule ",
        "RewriteCond "
    ],

    "access_controls": [
        "Order allow,deny",
        "Allow from all",
        "Deny from all",
        "Require all granted",
        "Require all denied"
    ],

    "misc_sensitive": [
        "SetEnv ",
        "SetEnvIf ",
        "Options +Indexes",
        "Options -Indexes",
        "DirectoryIndex "
    ]
}
