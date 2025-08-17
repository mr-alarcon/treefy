import argparse
from urllib.parse import urljoin

from cli.main_banner import create_main_banner
from cli.show_tree import show_tree
from core.get_url_list import get_url_list
from core.path_splitter import split_path
from core.directory_tree import create_directory_tree

parser = argparse.ArgumentParser(description="Get website tree")

parser.add_argument("-u", "--url", required=True, help="Enter URL")
parser.add_argument("-vc", "--verify-cert", action="store_true", help="Verify SSL certified")
parser.add_argument("-sb", "--show-banner", action="store_true", help="Show main banner")
parser.add_argument("-su", "--show-urls", action="store_true", help="Show URLs in the HTML source")
parser.add_argument("-st", "--show-tree", action="store_true", help="Show directory tree")
parser.add_argument("-em", "--emojis", action="store_true", help="Show directory tree emojis (folder/file)")


args = parser.parse_args()



if args.show_banner:
    create_main_banner()


if args.verify_cert:
    urls = get_url_list(args.url, True)
else:
    urls = get_url_list(args.url)


if args.show_urls:
    absolute_urls, relative_urls = split_path(urls)

    for url in relative_urls:
        full_url = urljoin(args.url + "/", url)
        print(full_url)

if args.show_tree:
    absolute_urls, relative_urls = split_path(urls)
    directory_tree = create_directory_tree(relative_urls)

    if args.emojis:
        show_tree(directory_tree, 1)
    else:
        show_tree(directory_tree, 2)




