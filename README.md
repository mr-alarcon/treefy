
## What is Treefy?

Treefy is a Python project whose main purpose is to **recreate the directory and file structure of a server**, as closely as possible to the original organization.

![gif](https://github.com/mr-alarcon/treefy/blob/legacy/media/last_gif.gif)

## How to work Treefy?

#### Create structure directories
Treefy sends a GET request to the target URL provided as a parameter and analyzes the site’s source code to find links, either in tags like `<a>` or in attributes such as `src`, `href`, `link`, or `iframe`. Once all URLs are collected, they are classified as absolute or relative, depending on whether they include the main domain at the beginning. 

Each URL is then split into segments corresponding to each part of its path; for example, `location/current/test.txt` becomes `'location'`, `'current'`, and `'test.txt'`. Each segment is converted into a dictionary key, whose value is another dictionary representing child directories or files. This process is performed recursively, generating a complete tree of the site’s directory structure.

At the end of the analysis, TreeFy provides a summary report including the total number of files, directories, discovered subdomains, and external domains found during the crawl.

![SCREENSHOT 1](https://raw.githubusercontent.com/mr-alarcon/treefy/refs/heads/legacy/media/last.png)


## Available Options

<table>
  <tr>
    <th>Argument</th>
    <th>Function</th>
  </tr>
  <tr>
    <td><code>-t</code>, <code>--tree</code></td>
    <td>
      Build the directory tree of the target website and show a summary
      of files, directories, subdomains, and external domains.
    </td>
  </tr>
</table>


---

**DISCLAIMER:** Treefy is intended for educational and authorized security research purposes only. 
It should only be used on systems you own or have explicit permission to test. 
The author is not responsible for any misuse, damage, or legal consequences arising from its use. 
Unauthorized use on systems without permission is illegal and may result in criminal and civil penalties.

