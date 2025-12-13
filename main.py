import argparse

def build_parser():        
    parser = argparse.ArgumentParser(description="Treefy by @mr-alarcon")

    parser_arguments = parser.add_argument_group("Flags")
    parser_arguments.add_argument("-u", "--url", metavar="URL", required=True, help="Target URL")
    parser_arguments.add_argument("-t", "--tree", action="store_true", help="Show directory tree")

    arguments = parser.parse_args()

    return arguments


def main():
    arguments = build_parser()


if __name__ == "__main__":
    main()