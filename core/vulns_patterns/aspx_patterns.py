vulns_patterns_aspx_dict = {

    "sql_injection": [
        "SqlCommand(",
        "ExecuteReader(",
        "ExecuteNonQuery(",
        "ExecuteScalar(",
        "DataAdapter(",
        "\"SELECT * FROM",
        "\"INSERT INTO",
        "\"UPDATE ",
        "\"DELETE FROM",
        "+ Request.QueryString",
        "+ Request.Form"
    ],

    "file_inclusion": [
        "Server.Execute(",
        "Server.Transfer(",
        "Server.MapPath("
    ],

    "command_execution": [
        "System.Diagnostics.Process.Start(",
        "Process.Start(",
        "System.Diagnostics.Process"
    ],

    "info_disclosure": [
        "Response.Write(",
        "Response.Output.Write(",
        "Trace.Write(",
        "Trace.Warn(",
        "Server.GetLastError()"
    ],

    "auth_risks": [
        "FormsAuthentication.SetAuthCookie(",
        "FormsAuthentication.RedirectFromLoginPage(",
        "Session[",
        "Response.Redirect(",
        "Request.Cookies(",
        "Response.Cookies("
    ],

    "file_system_risks": [
        "System.IO.File.ReadAllText(",
        "System.IO.File.ReadAllLines(",
        "System.IO.File.WriteAllText(",
        "System.IO.File.AppendAllText(",
        "System.IO.File.Delete(",
        "System.IO.Directory.Delete("
    ],

    "serialization_risks": [
        "BinaryFormatter.Deserialize(",
        "LosFormatter.Deserialize(",
        "JavaScriptSerializer.Deserialize(",
        "XmlSerializer.Deserialize("
    ],

    "mail_risks": [
        "System.Net.Mail.SmtpClient(",
        "System.Web.Mail.SmtpMail.Send("
    ],

    "misc_insecure": [
        "Eval(",
        "Execute(",
        "On Error Resume Next"
    ]
}
