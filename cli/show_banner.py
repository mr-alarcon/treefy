"""
Module: show_banner.py
Author: @mr-alarcon

Description:
    Provides a function to display the main banner of the Treefy
    CLI.
    
Functions:
    show_banner():
        Prints the colored banner in the CLI.
"""

# Standard library imports
from colorama import Fore

# Function to show the banner
def show_banner():
    
    print(f"""               
               {Fore.GREEN}░░░░░░░░░░░░░░░░░░░░
            ░░░░░░░░░░░░{Fore.YELLOW}┃{Fore.GREEN}░{Fore.YELLOW}┃{Fore.GREEN}░░░{Fore.RED}◎{Fore.GREEN}░░░░░░
          ░░░░░░░░░░░░░░{Fore.YELLOW}┃{Fore.GREEN}░{Fore.YELLOW}┃{Fore.GREEN}░░░{Fore.YELLOW}│{Fore.GREEN}░░░░░░░░░
        ░░░░░░░░░░░░░░░░{Fore.YELLOW}┃{Fore.GREEN}░{Fore.YELLOW}┃┬──┘{Fore.GREEN}░░░░░░░░░
            ░░░░░░░░░░░░{Fore.YELLOW}┃{Fore.GREEN}░{Fore.YELLOW}┃└──{Fore.GREEN}░░░░░░░░░
            ░░░░░{Fore.RED}◎{Fore.GREEN}░░░░░░{Fore.YELLOW}┃{Fore.GREEN}░{Fore.YELLOW}┃{Fore.GREEN}░░░░{Fore.RED}◎{Fore.GREEN}░░░░░░░░
            ░░░░░░░░░░░░{Fore.YELLOW}┃{Fore.GREEN}░{Fore.YELLOW}┃{Fore.GREEN}░░{Fore.YELLOW}┼──┘{Fore.GREEN}░░░░░░░░
            ░░░░░░░░░{Fore.YELLOW}└┐{Fore.GREEN}░{Fore.YELLOW}┃{Fore.GREEN}░{Fore.YELLOW}┃┌┴┴{Fore.GREEN}░░░{Fore.RED}◎{Fore.GREEN}░░░░░░░░
        ░░░░░░░{Fore.YELLOW}│{Fore.GREEN}░░░░░░{Fore.YELLOW}└─┃{Fore.GREEN}░{Fore.YELLOW}┃┴{Fore.GREEN}░░░░░░░░░░▒░░░░░
       ░░▒░░░{Fore.YELLOW}│{Fore.GREEN}░{Fore.YELLOW}│{Fore.GREEN}░░░░░░░░{Fore.YELLOW}┃{Fore.GREEN}░{Fore.YELLOW}┃{Fore.GREEN}░░░░░{Fore.RED}◎{Fore.GREEN}░░░░░░░░░░
       ░░░░░░{Fore.YELLOW}└─┤{Fore.GREEN}░░{Fore.RED}◎{Fore.GREEN}░░░{Fore.YELLOW}│{Fore.GREEN}░{Fore.YELLOW}┃{Fore.GREEN}░{Fore.YELLOW}┃{Fore.GREEN}░░░░░░░░░░░░░░░              
         ░░░░░░{Fore.YELLOW}└█{Fore.GREEN}░{Fore.YELLOW}│{Fore.GREEN}░░░{Fore.YELLOW}│{Fore.GREEN}░{Fore.YELLOW}▌{Fore.GREEN}░{Fore.YELLOW}▌{Fore.GREEN}░░░░░░{Fore.YELLOW}│{Fore.GREEN}░{Fore.YELLOW}│{Fore.GREEN}░░░░░░
          ░░░░░{Fore.YELLOW}──█┘{Fore.GREEN}░{Fore.RED}◎{Fore.GREEN}░{Fore.YELLOW}┴─█{Fore.GREEN}░{Fore.YELLOW}█{Fore.GREEN}░░░░░░{Fore.YELLOW}█─┴─{Fore.GREEN}░░░░░░
         ░░{Fore.YELLOW}└█{Fore.GREEN}░░░ {Fore.YELLOW}█ {Fore.GREEN}░░░░░{Fore.YELLOW}▀██─┘┌┘{Fore.GREEN}░{Fore.YELLOW}█┘{Fore.GREEN}░░░░░{Fore.YELLOW}▄┴{Fore.GREEN}░
         {Fore.YELLOW}└───█▄▄▄▄█{Fore.GREEN}░{Fore.YELLOW}┬┘{Fore.GREEN}░░░{Fore.YELLOW}██──┘{Fore.GREEN}░░{Fore.YELLOW}█{Fore.GREEN}░░{Fore.YELLOW}▄▄▄█
                  {Fore.YELLOW}█─┘{Fore.GREEN}░░░░{Fore.YELLOW}██▄{Fore.GREEN}░░░{Fore.YELLOW}█  █  
                   {Fore.YELLOW}▀▀▀▀▀████▀▀▀ ▀▀ 
                        ████            └─┤  {Fore.GREEN}mr-alarcon{Fore.YELLOW}
                        ████     ┌─┘      └──┼─────┬────┴
                        █████────┴──┤ {Fore.GREEN}Treefy{Fore.YELLOW} │     {Fore.RED}◎{Fore.YELLOW}
                        ████        └────────┴─ 
                        ████
                      ▒▒████▒▒
               ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓""")