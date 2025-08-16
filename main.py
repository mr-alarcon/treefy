import argparse
from urllib.parse import urljoin

from cli.main_banner import create_main_banner
from core.get_url_list import get_url_list
from core.path_splitter import split_path


parser = argparse.ArgumentParser(description="Get website tree")

parser.add_argument("-u", "--url", required=True, help="Enter URL")
parser.add_argument("-sb", "--show-banner", action="store_true", help="Show main banner")
parser.add_argument("-su", "--show-urls", action="store_true", help="Show URLs in the HTML source")
parser.add_argument("-st", "--show-tree", action="store_true", help="Show directory tree")

args = parser.parse_args()



if args.show_banner:
    create_main_banner()


if args.show_urls:
    urls = get_url_list(args.url)
    absolute_urls, relative_urls = split_path(urls)

    for url in relative_urls:
        full_url = urljoin(args.url + "/", url)
        print(full_url)