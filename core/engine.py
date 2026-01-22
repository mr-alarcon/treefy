"""
This module coordinates the main execution flow of the application
"""

from core.target_status import check_status_code
from discovery.urls import extract_urls, filter_urls, normalize_urls, deduplicate_urls
from analysis.classifier import classifier_urls
from features.tree_builder import tree_builder, add_files_to_tree

from output.tree_printer import print_tree

def run(url, tree, clone_tree):
    status, code = check_status_code(url)

    if status:
        urls_found = extract_urls(url)
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
    
    if tree:
        print_tree(tree_structure)
        print(f"\n{directory_count} directories, {files_count} files, {subdomains_count} subdomains, {external_domains_count} external domains")

    if clone_tree:
        pass


        



    