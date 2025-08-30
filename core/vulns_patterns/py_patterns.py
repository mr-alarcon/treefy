vulns_patterns_py_dict = {

    "sql_injection": [
        "cursor.execute(",
        "cursor.executemany(",
        "Session.execute(",
        "f\"SELECT ",
        "\"SELECT ",
        "format(",
        "%s\" % "
    ],

    "command_execution": [
        "os.system(",
        "subprocess.call(",
        "subprocess.run(",
        "subprocess.Popen(",
        "subprocess.check_output(",
        "commands.getoutput(",
        "commands.getstatusoutput("
    ],

    "eval_risks": [
        "eval(",
        "exec(",
        "compile("
    ],

    "file_system_risks": [
        "open(",
        "os.remove(",
        "os.unlink(",
        "os.rmdir(",
        "shutil.rmtree(",
        "os.rename(",
        "os.chmod(",
        "os.chown(",
        "tempfile.mktemp("
    ],

    "deserialization_risks": [
        "pickle.load(",
        "pickle.loads(",
        "cPickle.load(",
        "cPickle.loads(",
        "yaml.load(",
        "marshal.load(",
        "marshal.loads(",
        "dill.load(",
        "dill.loads("
    ],

    "insecure_network": [
        "requests.get(\"http://",
        "requests.post(\"http://",
        "urllib.request.urlopen(\"http://",
        "httplib.HTTPConnection(",
        "http.client.HTTPConnection("
    ],

    "crypto_risks": [
        "md5(",
        "sha1(",
        "random.random(",
        "random.randrange(",
        "random.randint(",
        "random.uniform("
    ],

    "info_disclosure": [
        "traceback.print_exc(",
        "logging.basicConfig(",
        "print("
    ],

    "auth_risks": [
        "SECRET_KEY =",
        "DEBUG = True",
        "ALLOWED_HOSTS = []",
        "app.secret_key ="
    ]
}
