vulns_patterns_jsp_dict = {

    "sql_injection": [
        "Statement.executeQuery(",
        "Statement.executeUpdate(",
        "Statement.execute(",
        "PreparedStatement.execute(",
        "PreparedStatement.executeQuery(",
        "PreparedStatement.executeUpdate(",
        "\"SELECT * FROM",
        "\"INSERT INTO",
        "\"UPDATE ",
        "\"DELETE FROM",
        "request.getParameter("
    ],

    "file_inclusion": [
        "RequestDispatcher.include(",
        "RequestDispatcher.forward(",
        "getServletContext().getResourceAsStream("
    ],

    "command_execution": [
        "Runtime.getRuntime().exec(",
        "ProcessBuilder("
    ],

    "info_disclosure": [
        "out.println(",
        "response.getWriter().println(",
        "e.printStackTrace(",
        "System.out.println(",
        "System.err.println("
    ],

    "auth_risks": [
        "session.getAttribute(",
        "session.setAttribute(",
        "request.getSession(",
        "response.sendRedirect(",
        "request.getCookies(",
        "response.addCookie("
    ],

    "file_system_risks": [
        "FileInputStream(",
        "FileOutputStream(",
        "FileReader(",
        "FileWriter(",
        "Files.readAllBytes(",
        "Files.write(",
        "new File(",
        "file.delete("
    ],

    "serialization_risks": [
        "ObjectInputStream(",
        "readObject("
    ],

    "mail_risks": [
        "javax.mail.Transport.send("
    ],

    "misc_insecure": [
        "ScriptEngineManager(",
        "engine.eval("
    ]
}
