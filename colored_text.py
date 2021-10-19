# colored text using Python

import colorama
from colorama import Fore,Back,Style

colorama.init(autoreset=True)

print(Fore.BLUE+Back.YELLOW+"Hi, My Name is Dhiraj"+
    Fore.YELLOW+Back.BLUE+ "I am handling Python time")

print(Back.CYAN+"Python is fun to learn")

print(Fore.RED+Back.GREEN+"I'm using To learn Python")
print(Style.BRIGHT+ "This is text in bright")
print(Style.DIM+"This is text in dim ")

print(Style.NORMAL+ "This is text in normal")
