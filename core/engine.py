"""
This module coordinates the main execution flow of the application
"""

import sys

from core.target_status import check_status_code
from discovery.urls import extract_urls, filter_urls, normalize_urls, deduplicate_urls
from analysis.classifier import classifier_urls
from utils.filters import matches_details_filters

from features.tree_builder import tree_builder, add_files_to_tree
from features.tree_cloner import create_base_path, tree_cloner
from features.output_file import save_output_file
from features.file_details import file_details

from output.tree_printer import print_tree
from output.files_details_printer import print_file_details

def run(url, tree, clone_tree, output_file, details, details_name, details_ext, details_risk, emojis, allow_redirect):
    status, code = check_status_code(url, allow_redirect)

    if status:
        urls_found = extract_urls(url, allow_redirect)
        urls_filtered = filter_urls(urls_found)
        urls_normalized = normalize_urls(url, urls_filtered)
        urls_deduplicated = deduplicate_urls(urls_normalized)

        files_urls, directory_urls, subdomains_urls, external_domains_urls = classifier_urls(url, urls_deduplicated)

        files_count = len(files_urls)
        directory_count = len(directory_urls)
        subdomains_count = len(subdomains_urls)
        external_domains_count = len(external_domains_urls)

        directory_structure = tree_builder(directory_urls)
        tree_structure = add_files_to_tree(directory_structure, files_urls)
    else:
        print(f"[!] Target not accessible ({code})")
        return 
    
    if output_file:
        save_output_file(output_file)
    
    if tree:
        print_tree(tree_structure, emojis, "")
        print(f"\n{directory_count} directories, {files_count} files, {subdomains_count} subdomains, {external_domains_count} external domains")

    if clone_tree:
        base_path = create_base_path(url, clone_tree)
        tree_cloner(tree_structure, base_path, allow_redirect)

    if details:
        files_details = file_details(files_urls)
        for file_info in files_details:
            if not matches_details_filters(
                file_info,
                details_name,
                details_ext,
                details_risk
            ):
                continue

            print_file_details(file_info)

    sys.stdout.close()

  