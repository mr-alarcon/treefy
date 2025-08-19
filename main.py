import argparse
from urllib.parse import urljoin

from cli.main_banner import create_main_banner
from cli.show_tree import show_tree
from core.get_url_list import get_url_list
from core.get_file_list import get_file_list
from core.path_splitter import split_path
from core.directory_tree import create_directory_tree

parser = argparse.ArgumentParser(description="Treefy by @mr-alarcon")

config_group = parser.add_argument_group("Configurations")
config_group.add_argument("-u", "--url", required=True, help="Target URL")
config_group.add_argument("-v", "--verify-cert", action="store_true", help="Verify SSL certificate")

output_group = parser.add_argument_group("Outputs")
output_group.add_argument("-b", "--banner", action="store_true", help="Show main banner")
output_group.add_argument("-e", "--emojis", action="store_true", help="Show emojis in the directory tree")
output_group.add_argument("-l", "--list-urls", action="store_true", help="List URLs found in the HTML source")
output_group.add_argument("-t", "--tree", action="store_true", help="Show directory tree")
output_group.add_argument("-f", "--files", action="store_true", help="Show files sumary")

args = parser.parse_args()



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








