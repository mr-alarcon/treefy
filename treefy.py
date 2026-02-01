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
    parser_arguments.add_argument("-d", "--details", action="store_true", help="Show details for discovered files")
    parser_arguments.add_argument("--details-name", nargs="?", metavar="NAME", help="Filter detailed output by file name")
    parser_arguments.add_argument("--details-ext", nargs="?", metavar="EXT", help="Filter detailed output by file extension")
    parser_arguments.add_argument("--details-risk", nargs="?", metavar="LEVEL", help="Filter detailed output by extension risk level")
    parser_arguments.add_argument("-c", "--clone-tree", nargs="?", const="./clones/", metavar="PATH", help="Clone directory tree")
    parser_arguments.add_argument("-o", "--output-file", nargs="?", metavar="PATH", help="Save output to file")
    parser_arguments.add_argument("-e", "--emojis", action="store_true", help="Show emojis in the directory tree")
    arguments = parser.parse_args()

    if (arguments.details_name or arguments.details_ext or arguments.details_risk) and not arguments.details:
        parser.error("--details is required when using detail filters")

    if arguments.emojis and not arguments.tree:
        parser.error("--tree is required when using emojis option")


    return arguments


def main():
    arguments = build_parser()
    
    url = arguments.url
    tree = arguments.tree
    details = arguments.details
    details_name = arguments.details_name
    details_ext = arguments.details_ext
    details_risk = arguments.details_risk
    clone_tree = arguments.clone_tree
    output_file = arguments.output_file
    emojis = arguments.emojis

    run(url, 
        tree, 
        clone_tree, 
        output_file,
        details,
        details_name,
        details_ext,
        details_risk,
        emojis,
        )


if __name__ == "__main__":
    main()