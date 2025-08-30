vulns_patterns_pl_dict = {

    "sql_injection": [
        "SELECT * FROM",
        "INSERT INTO",
        "UPDATE ",
        "DELETE FROM",
        "dbi->prepare(",
        "dbi->do(",
        "execute("
    ],

    "file_inclusion": [
        "require ",
        "use ",
        "do ",
        "require_once("
    ],

    "command_execution": [
        "system(",
        "exec(",
        "qx/",
        "open(.*\\|)",
        "open(\\|.*)",
        "popen(",
        "backticks"
    ],

    "eval_risks": [
        "eval ",
        "string eval"
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
        "$ENV{'REMOTE_ADDR'}",
        "$ENV{'QUERY_STRING'}"
    ],

    "file_system_risks": [
        "unlink(",
        "rename(",
        "mkdir(",
        "rmdir(",
        "chmod(",
        "chown(",
        "symlink(",
        "readlink(",
        "open("
    ],

    "serialization_risks": [
        "Storable::thaw(",
        "Storable::retrieve("
    ],

    "mail_risks": [
        "sendmail",
        "Mail::Send",
        "Mail::Mailer",
        "open(MAIL,"
    ],

    "misc_insecure": [
        "$ENV{'PATH_INFO'}",
        "$ENV{'SCRIPT_FILENAME'}",
        "$ENV{'DOCUMENT_ROOT'}",
        "$ENV{'SERVER_SOFTWARE'}"
    ]
}
