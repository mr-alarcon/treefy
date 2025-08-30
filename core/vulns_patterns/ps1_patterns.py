vulns_patterns_ps1_dict = {

    "command_execution": [
        "Invoke-Expression",
        "iex ",
        "Start-Process",
        "New-Object System.Net.WebClient",
        "Invoke-WebRequest",
        "Invoke-RestMethod",
        "cmd.exe",
        "powershell.exe",
        "Add-Type",
        "RunspaceInvoke"
    ],

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
    ]
}
