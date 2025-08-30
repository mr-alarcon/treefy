import requests
from urllib.parse import urlparse
from pathlib import Path

from core.get_url_file import get_url_files
from core.extensions_files import binary_exts

from core.vulns_patterns import (asp_patterns, aspx_patterns, bak_patterns, cgi_patterns,
                                 config_patterns, doc_patterns, env_patterns, git_patterns,
                                 htaccess_patterns, htpasswd_patterns, html_patterns, htm_patterns,
                                 inc_patterns, ini_patterns, js_patterns, json_patterns, jsp_patterns,
                                 key_patterns, log_patterns, old_patterns, p12_patterns, pdf_patterns,
                                 pem_patterns, pfx_patterns, php_pattterns, pl_patterns, ppt_patterns,
                                 pptx_patterns, ps1_patterns, py_patterns, rb_patterns, sh_patterns, 
                                 svg_patterns, tpl_patterns, xls_patterns, xlsx_patterns, xml_patterns,
                                 yaml_patterns, yml_patterns)



def scan_files(absolute_urls):
    global url_files

    patterns_dict = {
        "asp": asp_patterns.vulns_patterns_asp_dict,
        "aspx": aspx_patterns.vulns_patterns_aspx_dict,
        "bak": bak_patterns.vulns_patterns_bak_dict,
        "cgi": cgi_patterns.vulns_patterns_cgi_dict,
        "config": config_patterns.vulns_patterns_config_dict,
        "doc": doc_patterns.vulns_patterns_doc_dict,
        "env": env_patterns.vulns_patterns_env_dict,
        "git": git_patterns.vulns_patterns_git_dict,
        "htaccess": htaccess_patterns.vulns_patterns_htaccess_dict,
        "htpasswd": htpasswd_patterns.vulns_patterns_htpasswd_dict,
        "html": html_patterns.vulns_patterns_html_dict,
        "htm": htm_patterns.vulns_patterns_htm_dict,
        "inc": inc_patterns.vulns_patterns_inc_dict,
        "ini": ini_patterns.vulns_patterns_ini_dict,
        "js": js_patterns.vulns_patterns_js_dict,
        "json": json_patterns.vulns_patterns_json_dict,
        "jsp": jsp_patterns.vulns_patterns_jsp_dict,
        "key": key_patterns.vulns_patterns_key_dict,
        "log": log_patterns.vulns_patterns_log_dict,
        "old": old_patterns.vulns_patterns_old_dict,
        "p12": p12_patterns.vulns_patterns_p12_dict,
        "pdf": pdf_patterns.vulns_patterns_pdf_dict,
        "pem": pem_patterns.vulns_patterns_pem_dict,
        "pfx": pfx_patterns.vulns_patterns_pfx_dict,
        "php": php_pattterns.vulns_patterns_php_dict,
        "pl": pl_patterns.vulns_patterns_pl_dict,
        "ppt": ppt_patterns.vulns_patterns_ppt_dict,
        "pptx": pptx_patterns.vulns_patterns_pptx_dict,
        "ps1": ps1_patterns.vulns_patterns_ps1_dict,
        "py": py_patterns.vulns_patterns_py_dict,
        "rb": rb_patterns.vulns_patterns_rb_dict,
        "sh": sh_patterns.vulns_patterns_sh_dict,
        "svg": svg_patterns.vulns_patterns_svg_dict,
        "tpl": tpl_patterns.vulns_patterns_tpl_dict,
        "xls": xls_patterns.vulns_patterns_xls_dict,
        "xlsx": xlsx_patterns.vulns_patterns_xlsx_dict,
        "xml": xml_patterns.vulns_patterns_xml_dict,
        "yaml": yaml_patterns.vulns_patterns_yaml_dict,
        "yml": yml_patterns.vulns_patterns_yml_dict
    }

    # Retrieve all files (URLs) from the given list of absolute URLs
    url_files = get_url_files(absolute_urls)

    # Iterate over each file obtained
    for key, value in url_files.items():

        # Skip binary files (e.g., images, executables, etc.)
        if key.split("?")[0].endswith(binary_exts):
            continue
        else:
            # Send a GET request to fetch the file contents
            response = requests.get(value)

            path_file = urlparse(value).path 
            clean_file = Path(path_file).name 
            ext_pattern = Path(clean_file).suffix.lstrip(".").lower()

            for line_num, line in enumerate(response.text.splitlines(), start=1):
                for type_vuln, content_vuln in patterns_dict[ext_pattern].items():
                    for pattern_vuln in content_vuln:
                        if pattern_vuln in line:
                            print(f"File: {key}")
                            print(f"Vuln Type: {type_vuln}")
                            print(f"Vuln Cont: {pattern_vuln}")
                            print(f"Line #: {line_num}")
                            print(f"Line: {line}")
                        else:
                            continue

                        print("===========================================================")
