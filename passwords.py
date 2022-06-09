import os
from colorama import Fore

done = False

delete = input(Fore.CYAN + "Delete password file? [y/n]: ")
if delete == "y":
    # Checking if the file exists and if it does it deletes it.
    if os.path.exists("pwds.txt") == True:
        os.remove("pwds.txt")
        print(Fore.RED + "[ALERT] >>> " + Fore.YELLOW + "Passwords deleted!")
        exit()
    else:
        print(Fore.MAGENTA + "[CRTITCAL] >>> " + Fore.YELLOW +  "Password file does not exist")
        cont = input(Fore.RED + "[ALERT] >>> " + Fore.YELLOW + "Write password list? [y/n]: ")
        if cont == "n":
            exit()
read = input("Read password file? [y/n]: ")
if read == "y":
    pwdfile = open("pwds.txt", "r")
    for z in pwdfile.read().split(","):
        print(z)

print(Fore.GREEN + "Please type in passwords one by one")
print(Fore.RED + "[ALERT] >>> " + Fore.YELLOW + "When complete type done!")

overide = input(Fore.RED + "[CRTITCAL] >>> " + Fore.YELLOW + "Overide Password Store file? [y/n]: ")
if overide == "y":
    pwdfile = open("pwds.txt", "w")
    pwdfile.write("")
    pwdfile.close()

pwdfile = open("pwds.txt", "a")
# Asking for a password and then writing it to a file.
while done == False:
    pwd = input(Fore.CYAN + "Password: ")
    pwdfile.write(pwd + ", ")
    if pwd == "done" or "":
        pwdfile.close()
        break
    else:
        continue