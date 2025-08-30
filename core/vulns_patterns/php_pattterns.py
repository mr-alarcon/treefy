vulns_patterns_php_dict = {

    "sql_injection": [
        "mysql_query(",
        "mysqli_query(",
        "pg_query(",
        "odbc_exec(",
        "oci_parse(",
        "PDO->query(",
        "PDO->exec(",
        "$_GET",
        "$_POST",
        "$_REQUEST"
    ],

    "file_inclusion": [
        "include(",
        "include_once(",
        "require(",
        "require_once(",
        "fopen(",
        "file_get_contents(",
        "readfile(",
        "opendir(",
        "readdir("
    ],

    "command_execution": [
        "exec(",
        "shell_exec(",
        "system(",
        "passthru(",
        "popen(",
        "proc_open("
    ],

    "eval_risks": [
        "eval(",
        "create_function("
    ],

    "info_disclosure": [
        "phpinfo(",
        "var_dump(",
        "print_r(",
        "error_reporting(",
        "ini_set("
    ],

    "auth_risks": [
        "setcookie(",
        "header(",
        "session_start(",
        "session_id(",
        "unserialize("
    ],

    "file_system_risks": [
        "unlink(",
        "fwrite(",
        "fputs(",
        "file_put_contents(",
        "chmod(",
        "chown(",
        "mkdir(",
        "rmdir("
    ],

    "serialization_risks": [
        "unserialize(",
        "serialize("
    ],

    "mail_risks": [
        "mail("
    ],

    "misc_insecure": [
        "assert(",
        "preg_replace(",
        "dl("
    ]
}
