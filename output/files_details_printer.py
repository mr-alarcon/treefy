def print_file_details(file_info):
    print(f"-> {file_info.get('File name')}")
    for key, value in file_info.items():
        if key == "name":
            continue
        print(f"   - {key.replace('_', ' ').title()}: {value}")