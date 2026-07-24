from colorama import Fore, Back, Style
import colorama

colorama.init()

print(Fore.GREEN + "This text is green.")
print(Fore.RED + "This text is red.")
print(Fore.YELLOW + "This text is yellow.")
print(Fore.BLUE + "This text is blue.")
print(Style.RESET_ALL + "This text is back to normal.")

print(Back.GREEN + Fore.BLACK + "Green background with black text.")
print(Style.RESET_ALL)

print(Fore.RED + "ERROR: Something went wrong!")
print(Fore.GREEN + "SECCESS: Operation completed.")
print(Fore.YELLOW + "WARNING: Please check your input.")
print(Style.RESET_ALL) 
