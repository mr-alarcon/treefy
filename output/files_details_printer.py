def print_file_details(files_details):
    for file_info in files_details:
        for file_info_title, file_info_value in file_info.items():
            if file_info_title == "File name":
                print(f"-> {file_info_title}: {file_info_value}")
            else:
                print(f"   - {file_info_title}: {file_info_value}")