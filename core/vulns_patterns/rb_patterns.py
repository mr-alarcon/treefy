vulns_patterns_rb_dict = {

    "sql_injection": [
        "ActiveRecord::Base.connection.execute(",
        "Model.find_by_sql(",
        "Model.where(",
        "Model.find_by(",
        "exec_query(",
        "exec(",
        "%Q{SELECT ",
        "%Q{INSERT ",
        "%Q{UPDATE ",
        "%Q{DELETE ",
        "params[:"
    ],

    "command_execution": [
        "system(",
        "`",
        "exec(",
        "spawn(",
        "IO.popen(",
        "Open3.capture3(",
        "Open3.popen3("
    ],

    "eval_risks": [
        "eval(",
        "instance_eval(",
        "class_eval(",
        "module_eval("
    ],

    "file_system_risks": [
        "File.read(",
        "File.write(",
        "File.open(",
        "File.delete(",
        "Dir.mkdir(",
        "Dir.delete(",
        "FileUtils.rm_rf(",
        "FileUtils.chmod(",
        "FileUtils.chown("
    ],

    "serialization_risks": [
        "Marshal.load(",
        "Marshal.restore(",
        "YAML.load(",
        "YAML.safe_load(",
        "JSON.parse("
    ],

    "mail_risks": [
        "ActionMailer::Base.deliver_now(",
        "Net::SMTP.start(",
        "Mail.deliver("
    ],

    "info_disclosure": [
        "puts ",
        "p ",
        "warn ",
        "logger.debug(",
        "logger.info("
    ],

    "auth_risks": [
        "cookies[:",
        "session[:",
        "redirect_to(",
        "before_action :authenticate_user!"
    ],

    "misc_insecure": [
        "OpenStruct.new(",
        "Kernel.load(",
        "Kernel.require(",
        "load(",
        "require(",
        "instance_variable_set("
    ]
}
