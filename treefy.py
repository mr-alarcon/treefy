"""
Entry point
"""

import argparse

from core.engine import run

def build_parser():        
    parser = argparse.ArgumentParser(description="Treefy by @mr-alarcon",
                                     add_help=False,
                                     formatter_class=lambda prog: argparse.RawTextHelpFormatter(prog, max_help_position=40, width=100)
                                     )

    parser_arguments = parser.add_argument_group("Flags")
    parser_arguments.add_argument("-h", "--help", action="help", help="Show this help message")
    parser_arguments.add_argument("-u", "--url", metavar="URL", required=True, help="Target URL")
    parser_arguments.add_argument("-t", "--tree", action="store_true", help="Show directory tree")
    parser_arguments.add_argument("-c", "--clone-tree", nargs="?", const="./clones/", metavar="PATH", help="Clone directory tree")
    parser_arguments.add_argument("-o", "--output-file", nargs="?", metavar="PATH", help="Save output to file")

    arguments = parser.parse_args()

    return arguments


def main():
    arguments = build_parser()
    
    url = arguments.url
    tree = arguments.tree
    clone_tree = arguments.clone_tree
    output_file = arguments.output_file

    run(url, 
        tree, 
        clone_tree, 
        output_file,
        )


if __name__ == "__main__":
    main()