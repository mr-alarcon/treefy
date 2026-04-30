JS_PATTERNS = {
    "code_execution_sinks": [
        "eval(",
        "Function(",
        "setTimeout(",
        "setInterval(",
        "document.write(",
    ],

    "dom_xss": [
        "innerHTML",
        "outerHTML",
        "insertAdjacentHTML",
        "document.write",
    ],

    "sensitive_endpoints": [
        "/api/",
        "/admin",
        "/login",
        "/auth",
        "/config",
        "/internal",
    ],

    "debug_exposure": [
        "console.log(",
        "console.debug(",
        "debugger;",
    ],

    "insecure_requests": [
        "http://",
        "fetch(",
        "XMLHttpRequest(",
    ],

    "insecure_cookies": [
        "document.cookie",
    ],

    "exposed_config": [
        "ENV",
        "process.env",
        "NODE_ENV",
    ],
}