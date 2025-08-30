vulns_patterns_asp_dict = {
    "sql_injection": [
        "Request.QueryString",
        "Request.Form", 
        "SELECT * FROM",
        "INSERT INTO",
        "UPDATE ",
        "DELETE FROM",
        "& Request.QueryString(",
        "& Request.Form("
    ],

    "file_inclusion": [
        "Server.Execute(",
        "Server.Transfer(",
        "Include file="
    ],

    "command_execution": [
        "CreateObject(\"WScript.Shell\")",
        ".Run(",
        ".Exec(",
        "Shell.Application"
    ],

    "info_disclosure": [
        "Response.Write(",
        "Response.End(",
        "Response.Flush(",
        "Server.MapPath("
    ],

    "auth_risks": [
        "Session(\"",
        "Response.Redirect(",
        "Request.Cookies(",          
        "Response.Cookies("
    ],

    "file_system_risks": [
        "CreateObject(\"Scripting.FileSystemObject\")",
        ".CreateTextFile(",
        ".OpenTextFile(",
        ".DeleteFile(",
        ".DeleteFolder(",
        ".CopyFile("
    ],

    "mail_risks": [
        "CDO.Message",
        "CDONTS.NewMail",
    ],

    "misc_insecure": [
        "On Error Resume Next",
        "Eval(",                      
        "Execute("
    ]              
}
