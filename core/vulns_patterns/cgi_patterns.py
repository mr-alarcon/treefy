vulns_patterns_cgi_dict = {

    "sql_injection": [
        "SELECT * FROM",
        "INSERT INTO",
        "UPDATE ",
        "DELETE FROM",
        "db.execute(",
        "cursor.execute(",
        "$ENV{'QUERY_STRING'}",
        "$ENV{'REQUEST_METHOD'}",
        "$ENV{'CONTENT_LENGTH'}"
    ],

    "file_inclusion": [
        "open(",
        "require(",
        "do ",
        "use ",
        "require_once(",
        "include("
    ],

    "command_execution": [
        "system(",
        "exec(",
        "popen(",
        "passthru(",
        "qx/",
        "backticks (`command`)"
    ],

    "eval_risks": [
        "eval(",
        "do_eval("
    ],

    "info_disclosure": [
        "print ",
        "warn ",
        "die ",
        "Data::Dumper",
        "Carp::confess",
        "Carp::croak"
    ],

    "auth_risks": [
        "$ENV{'HTTP_COOKIE'}",
        "$ENV{'REMOTE_USER'}",
        "$ENV{'AUTH_TYPE'}",
        "$ENV{'REMOTE_ADDR'}"
    ],

    "file_system_risks": [
        "unlink(",
        "rename(",
        "mkdir(",
        "rmdir(",
        "chmod(",
        "chown(",
        "symlink(",
        "readlink("
    ],

    "serialization_risks": [
        "Storable::thaw(",
        "Storable::retrieve("
    ],

    "mail_risks": [
        "sendmail",
        "Mail::Send",
        "Mail::Mailer"
    ],

    "misc_insecure": [
        "$ENV{'PATH_INFO'}",
        "$ENV{'SCRIPT_FILENAME'}",
        "$ENV{'DOCUMENT_ROOT'}"
    ]
}
