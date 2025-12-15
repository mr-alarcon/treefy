> ⚠️ **Warning**
>
> This branch is **legacy** and contains partially implemented and outdated/empty functionality.
>
> For the stable version of the project, visit the [main branch](https://github.com/mr-alarcon/treefy/tree/main).


![README BANNER](https://raw.githubusercontent.com/mr-alarcon/treefy/refs/heads/legacy/media/readme_banner.gif)

## What is Treefy? (Under Development)

Treefy is a Python project whose main purpose is to **recreate the directory and file structure of a server**, as closely as possible to the original organization.

It also currently includes additional features such as **cloning the structure locally**, **analyzing the source code of each file** to detect potential vulnerabilities, and **categorizing files by extension** into *High/Medium/Low*, depending on how critical files of those types usually are.

To learn more about the current features and those under development, please refer to the **Features** section.

![SCREENSHOT 1](https://raw.githubusercontent.com/mr-alarcon/treefy/refs/heads/legacy/media/1.png)

---
## How to work Treefy?

#### Create structure directories
Treefy sends a GET request to the target URL provided as a parameter and analyzes the site’s source code to find links, either in tags like `<a>` or in attributes such as `src`, `href`, `link`, or `iframe`. Once all URLs are collected, they are classified as absolute or relative, depending on whether they include the main domain at the beginning. 

Each URL is then split into segments corresponding to each part of its path; for example, `location/current/test.txt` becomes `'location'`, `'current'`, and `'test.txt'`. Each segment is converted into a dictionary key, whose value is another dictionary representing child directories or files. This process is performed recursively, generating a complete tree of the site’s directory structure.

#### Verify SSL Certificate

The SSL certificate verification option uses the `verify` parameter of the `get` method from Python's standard `requests` library. This option is **disabled by default**, and to enable it, you must pass the `--verify-cert` parameter when running Treefy.

#### Clone Directory Structure

The local cloning of the directory structure follows the same process used to generate the tree with the `--tree` parameter. Treefy creates directories and files following the hierarchy of the generated tree. To determine if a path segment is a file or a directory, Treefy checks for the presence of a file extension. If it is a directory, a folder is created locally. If it is a file, a local file is created with the corresponding extension, and a request is made to the file's URL to copy its source code into the created file. For multimedia files, the same process is applied, but the source code is written in **binary mode** to preserve the file contents.

#### Scan Files

To scan files, Treefy first collects all URLs embedded in the website's source code and filters only those that point to files based on their extensions. Then, a dictionary is created where the key is the file name and the value is the file's URL. Treefy iterates over each file and then over each line of code within the file, comparing every line against the lists in the `vulns_patterns` dictionaries. If a line matches any pattern, Treefy reports a **possible vulnerability** in that file.


---
![SCREENSHOT 2](https://raw.githubusercontent.com/mr-alarcon/treefy/refs/heads/legacy/media/2.png)

## Features

These are the features currently available. Although they are not fully tested, they should work without major issues. Features marked with `*` are still under development.

- `--help` or `-h`
  Display all available parameters and options.

- `--url` or `-u`
  Specify the target URL to analyze. Example: `--url https://example.com`.

- `--verify-cert` or `-v`
  Enable SSL certificate verification for HTTPS sites.

- `--emojis` or `-e`
  Display emojis when using the `--tree` option to show the directory structure.

- `--list-urls` or `-l`
  List all URLs found in the website's source code.

- `--tree` or `-t`
  Display the directory structure (tree) of the website.

- `--files` or `-f`
  Show a summary of the found files, including: file name, file extension counts, and extension category (High, Medium, Low).

- `* --clone-tree` or `-c`
  Clone the directory structure locally.  
  Example: `python main.py -u https://example.com --clone-tree path/to/clone`

- `* --scan-files` or `-s`
  Scan each code file to detect possible vulnerabilities.

- `--output` or `-o`
  Save the CLI output to a file.  
  Example: `python main.py -u https://example.com --tree --output file.txt`

---
**DISCLAIMER:** Treefy is intended for educational and authorized security research purposes only. 
It should only be used on systems you own or have explicit permission to test. 
The author is not responsible for any misuse, damage, or legal consequences arising from its use. 
Unauthorized use on systems without permission is illegal and may result in criminal and civil penalties.
