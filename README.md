
## What is Treefy?

Treefy is a Python project whose main purpose is to **recreate the directory and file structure of a server**, as closely as possible to the original organization.

It also currently includes additional features such as **cloning the structure locally** and **categorizing files by extension** into *Critical/High/Medium/Low*, depending on how critical files of those types usually are.

To learn more about the current features and those under development, please refer to the **Features** section.

![gif](https://github.com/mr-alarcon/treefy/blob/legacy/media/last_gif.gif)

## How to work Treefy?

#### Create structure directories
Treefy sends a GET request to the target URL provided as a parameter and analyzes the site’s source code to find links, either in tags like `<a>` or in attributes such as `src`, `href`, `link`, or `iframe`. Once all URLs are collected, they are classified as absolute or relative, depending on whether they include the main domain at the beginning. 

Each URL is then split into segments corresponding to each part of its path; for example, `location/current/test.txt` becomes `'location'`, `'current'`, and `'test.txt'`. Each segment is converted into a dictionary key, whose value is another dictionary representing child directories or files. This process is performed recursively, generating a complete tree of the site’s directory structure.

At the end of the analysis, TreeFy provides a summary report including the total number of files, directories, discovered subdomains, and external domains found during the crawl.

#### Details for Discoverd files
The option to display details of discovered files in Treefy allows users to view additional information for each file found during the analysis. When enabled, the tool shows data such as the file name, its extension, the URL associated with the resource, file size, last modification time, and other relevant attributes, providing a more descriptive view of the discovered content. In addition, this option includes filters that allow only files with specific characteristics to be displayed (`--details-name`, `--details-ext`, `--details-risk`).

#### Clone Directory Structure
The local cloning of the directory structure follows the same process used to generate the tree with the `--tree` parameter. Treefy creates directories and files following the hierarchy of the generated tree. To determine if a path segment is a file or a directory, Treefy checks for the presence of a file extension. If it is a directory, a folder is created locally. If it is a file, a local file is created with the corresponding extension, and a request is made to the file's URL to copy its source code into the created file. For multimedia files, the same process is applied, but the source code is written in **binary mode** to preserve the file contents.

![SCREENSHOT 1](https://raw.githubusercontent.com/mr-alarcon/treefy/refs/heads/legacy/media/last.png)


## Features

<table>
  <tr>
    <th>Argument</th>
    <th>Function</th>
  </tr>
  <tr>
    <td><code>-t</code>, <code>--tree</code></td>
    <td>
      Build the directory tree of the target website and show a summary of files, directories, subdomains, and external domains.
    </td>
  </tr>

  <tr>
    <td><code>-d</code>, <code>--details</code></td>
     <td>
      Display discovered file details in Treefy provides additional information such as the file name, extension, URL, size and last modification time.
    </td>
  </tr>

  <tr>
    <td><code>--details-name</code></td>
     <td>
      Filter used together with the -d flag to display only files whose names match specific criteria during the detailed analysis.
    </td>
  </tr>

  <tr>
    <td><code>--details-ext</code></td>
     <td>
      Filter used together with the -d flag to display only files whose extensions match specific criteria during the detailed analysis.
    </td>
  </tr>

  <tr>
    <td><code>--details-risk</code></td>
     <td>
      Filter used together with the -d flag to display only files whose extension risk category match specific criteria during the detailed analysis.
    </td>
  </tr>

  <tr>
    <td><code>-c</code> <code>--clone-tree</code></td>
     <td>
      Allows replicate the discovered directory structure locally, creating folders and files based on the analyzed tree.
    </td>
  </tr>

  <tr>
    <td><code>-o</code> <code>--output-file</code></td>
     <td>
      Allows saving the generated output to a specified file rather than displaying it only in the terminal.
    </td>
  </tr>

  <tr>
    <td><code>-e</code> <code>--emojis</code></td>
     <td>
      Enables the use of emojis when displaying the directory tree output.
    </td>
  </tr>

</table>


---

> **DISCLAIMER:** 
> Treefy is intended for educational and authorized security research purposes only. 
> It should only be used on systems you own or have explicit permission to test. 
> The author is not responsible for any misuse, damage, or legal consequences arising from its use. 
> Unauthorized use on systems without permission is illegal and may result in criminal and civil penalties.

