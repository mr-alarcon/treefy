import argparse
import sys
from urllib.parse import urljoin

from cli.main_banner import create_main_banner
from cli.show_tree import show_tree
from core.get_url_list import get_url_list
from core.get_file_list import get_file_list
from core.path_splitter import split_path
from core.directory_tree import create_directory_tree
from core.local_clone_tree import create_local_clone_tree
from core.save_output import save_output_file
from core.scan_file import scan_files


parser = argparse.ArgumentParser(description="Treefy by @mr-alarcon")

config_group = parser.add_argument_group("Configurations")
config_group.add_argument("-u", "--url", metavar="URL", required=True, help="Target URL")
config_group.add_argument("-v", "--verify-cert", action="store_true", help="Verify SSL certificate")

output_group = parser.add_argument_group("Outputs")
output_group.add_argument("-b", "--banner", action="store_true", help="Show main banner")
output_group.add_argument("-e", "--emojis", action="store_true", help="Show emojis in the directory tree")
output_group.add_argument("-l", "--list-urls", action="store_true", help="List URLs found in the HTML source")
output_group.add_argument("-t", "--tree", action="store_true", help="Show directory tree")
output_group.add_argument("-f", "--files", action="store_true", help="Show files sumary")
output_group.add_argument("-c", "--clone-tree", metavar="PATH", type=str, help="Make a local clone tree")
output_group.add_argument("-s", "--scan-files", action="store_true", help="Scan code files to find vulnerabilities")
output_group.add_argument("-o", "--output", metavar="FILE", type=str, help="Save output to file")

args = parser.parse_args()



if args.output:
    save_output_file(args.output)

if args.banner:
    create_main_banner()

if args.verify_cert:
    urls = get_url_list(args.url, True)
else:
    urls = get_url_list(args.url)

if args.list_urls:
    _, relative_urls = split_path(urls)

    for url in relative_urls:
        full_url = urljoin(args.url + "/", url)
        print(full_url)

if args.tree:
    _, relative_urls = split_path(urls)
    directory_tree = create_directory_tree(relative_urls)

    if args.emojis:
        show_tree(directory_tree, 1)
    else:
        show_tree(directory_tree, 2)

if args.files:
    _, relative_urls = split_path(urls)
    files_dict = get_file_list(relative_urls)

    for main_key, main_value in files_dict.items():
        print(f"[+] Type: {main_key}")
        
        for key, value in main_value.items():
            if key == "Amount" or key == "Category":
                print(f"[+] {key}: {value}")
            else:
                print(f"[+] {key}:")
                
                for i in value:
                    print(f"  • {i}")
        print("\n")


if args.clone_tree:
    absolute_urls, relative_urls = split_path(urls)
    directory_tree = create_directory_tree(relative_urls)
    create_local_clone_tree(absolute_urls, directory_tree, args.clone_tree)
    

if args.scan_files:
    absolute_urls, _ = split_path(urls)
    scan_files(absolute_urls)