# Standard library imports
import argparse
import sys
from colorama import Fore as F
# Local modules imports
from cli.show_tree import show_tree
from cli.show_urls_list import show_urls_list
from cli.show_file_sumary import show_file_sumary
from cli.show_initial_info import show_initial_info

from core.get_url_list import get_url_list
from core.get_file_list import get_file_list
from core.path_splitter import split_path
from core.directory_tree import create_directory_tree
from core.local_clone_tree import create_local_clone_tree
from core.save_output import save_output_file
from core.scan_file import scan_files


# ---> Creation of CLI arguments to configure Treefy execution
parser = argparse.ArgumentParser(description="Treefy by @mr-alarcon")

config_group = parser.add_argument_group("Configurations")
config_group.add_argument("-u", "--url", metavar="URL", required=True, help="Target URL")
config_group.add_argument("-v", "--verify-cert", action="store_true", help="Verify SSL certificate")

output_group = parser.add_argument_group("Outputs")
output_group.add_argument("-e", "--emojis", action="store_true", help="Show emojis in the directory tree")
output_group.add_argument("-l", "--list-urls", action="store_true", help="List URLs found in the HTML source")
output_group.add_argument("-t", "--tree", action="store_true", help="Show directory tree")
output_group.add_argument("-f", "--files", action="store_true", help="Show files sumary")
output_group.add_argument("-c", "--clone-tree", metavar="PATH", type=str, help="Make a local clone tree")
output_group.add_argument("-s", "--scan-files", action="store_true", help="Scan code files to find vulnerabilities")
output_group.add_argument("-o", "--output", metavar="FILE", type=str, help="Save output to file")

args = parser.parse_args()


# --- If the user provides no reconnaissance parameters, show this message and exit.
if not any([args.list_urls, args.tree, args.files, args.clone_tree, args.scan_files]):
    print(f"{F.YELLOW}[!] {F.RED}No action was specified for the target. Please specify at least one reconnaissance option.{F.RESET}")
    sys.exit()

# Show initial input information
show_initial_info(args.url, args.verify_cert)

# ---> Execute the corresponding functions based on the parsed CLI arguments

# --- Verify SSL certified (True, False)
if args.verify_cert:
    urls = get_url_list(args.url, True)
else:
    urls = get_url_list(args.url)

# --- Save the output into a file
if args.output:
    save_output_file(args.output)

# --- List the source code URLs found
if args.list_urls:
    show_urls_list(urls, args.url)

# --- Show the website directory tree
if args.tree:
    show_tree(urls, args.emojis)

# --- Show a summary of all files found
if args.files:
    show_file_sumary(urls)

# --- Clone the website tree locally
if args.clone_tree:
    create_local_clone_tree(urls, args.clone_tree, True, args.url)
    
# --- Scan each file of the website
if args.scan_files:
    absolute_urls, _ = split_path(urls)
    scan_files(absolute_urls)
