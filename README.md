
## What is Treefy?

Treefy is a Python project whose main purpose is to **recreate the directory and file structure of a server**, as closely as possible to the original organization.

![gif](https://raw.githubusercontent.com/mr-alarcon/treefy/refs/heads/legacy/media/using_treefy.gif)

## How to work Treefy?

#### Create structure directories
Treefy sends a GET request to the target URL provided as a parameter and analyzes the site’s source code to find links, either in tags like `<a>` or in attributes such as `src`, `href`, `link`, or `iframe`. Once all URLs are collected, they are classified as absolute or relative, depending on whether they include the main domain at the beginning. 

Each URL is then split into segments corresponding to each part of its path; for example, `location/current/test.txt` becomes `'location'`, `'current'`, and `'test.txt'`. Each segment is converted into a dictionary key, whose value is another dictionary representing child directories or files. This process is performed recursively, generating a complete tree of the site’s directory structure.

![SCREENSHOT 1](https://raw.githubusercontent.com/mr-alarcon/treefy/refs/heads/legacy/media/treefy_cap3.png)

---


**DISCLAIMER:** Treefy is intended for educational and authorized security research purposes only. 
It should only be used on systems you own or have explicit permission to test. 
The author is not responsible for any misuse, damage, or legal consequences arising from its use. 
Unauthorized use on systems without permission is illegal and may result in criminal and civil penalties.

