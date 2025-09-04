from colorama import Fore as F


def show_initial_info(target, verify_cert):
    print(f"{F.YELLOW}[+] {F.WHITE}URL target> {F.GREEN}{target}{F.RESET}")
    print(f"{F.YELLOW}[!] {F.WHITE}If the website give {F.GREEN}403{F.WHITE}, {F.GREEN}302 {F.WHITE}or {F.GREEN}303 {F.WHITE}error code maybe you need to use the {F.GREEN}-a {F.WHITE}or {F.GREEN}-v {F.WHITE}flags{F.RESET}")
    
    if verify_cert:
        print(f"{F.YELLOW}[!] {F.WHITE}Verify SSL certified to the target")
    else:
        pass