import argparse

from cli.main_banner import create_main_banner
from core.get_url_list import get_url_list

parser = argparse.ArgumentParser(description="Get website tree")

parser.add_argument("-u", "--url", required=True, help="Enter URL")
parser.add_argument("-sb", "--show-banner", action="store_true", help="Show main banner")
parser.add_argument("-st", "--show-tree", action="store_true", help="Show directory tree")

args = parser.parse_args()

urls = get_url_list(args.url)

if args.show_banner:
    create_main_banner()


print(urls)