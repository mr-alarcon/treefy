"""
Entry point
"""

import argparse

from core.engine import run

def build_parser():        
    parser = argparse.ArgumentParser(description="Treefy by @mr-alarcon",
                                     add_help=False,
                                     usage="treefy.py [-h] [-u TARGET] [-d] [--details-name NAME] [--details-ext EXT] [--details-risk LVL] [-c PATH] [-o FILE] [-e] [--allow-redirect] [--verify-cert]",
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
    parser_arguments.add_argument("-o", "--output-file", nargs="?", metavar="FILE", help="Save output to file")
    parser_arguments.add_argument("-e", "--emojis", action="store_true", help="Show emojis in the directory tree")
    parser_arguments.add_argument("--allow-redirect", action="store_true", help="Follow redirects when enabled")
    parser_arguments.add_argument("--verify-cert", action="store_true", help="Require valid SSL/TLS certificate")
    arguments = parser.parse_args()

    if (arguments.details_name or arguments.details_ext or arguments.details_risk) and not arguments.details:
        parser.error("--details is required when using detail filters")

    if arguments.emojis and not arguments.tree:
        parser.error("--tree is required when using emojis option")


    return arguments


def main():
    arguments = build_parser()
    

    run(
        arguments.url, 
        arguments.tree, 
        arguments.clone_tree, 
        arguments.output_file,
        arguments.details,
        arguments.details_name,
        arguments.details_ext,
        arguments.details_risk,
        arguments.emojis,
        arguments.allow_redirect,
        arguments.verify_cert,
        )


if __name__ == "__main__":
    main()