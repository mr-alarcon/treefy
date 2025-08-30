vulns_patterns_js_dict = {
    "dynamic_execution": [
        "eval(",
        "new Function(",
        "setTimeout(",
        "setInterval("
    ],

    "dom_injection": [
        "document.write(",
        "document.writeln(",
        ".innerHTML",
        ".outerHTML"
    ],

    "storage_risks": [
        "localStorage.setItem(",
        "sessionStorage.setItem(",
        "document.cookie"
    ],

    "insecure_redirects": [
        "window.location",
        "location.href",
        "document.location",
        "window.open("
    ],

    "insecure_resources": [
        'fetch("http://',
        'fetch(\'http://',
        '$.get("http://',
        '$.get(\'http://',
        'xhr.open("GET", "http://',
        'xhr.open(\'GET\', \'http://'
    ],

    "nodejs_risks": [
        "require(",               
        "child_process.exec(",    
        "child_process.execSync(",
        "child_process.spawn(", 
        "fs.readFile(",           
        "fs.readFileSync(",
        "fs.writeFile(",
        "fs.writeFileSync(",
        "child_process.execFile(",
        "process.env["
    ],

    "regex_risks": [
        "new RegExp("
    ],

    "frontend_risks": [
        "with(",            
        "insertAdjacentHTML",
        "location.assign("
    ]
}