# A password manager.
import os
from colorama import Fore
import string  
import secrets 

done = False
def writePass():
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

delete = input(Fore.CYAN + "Delete password file? [y/n]: ")
# Checking if the file exists and if it does it deletes it.
if delete == "y":
    # Checking if the file exists and if it does it deletes it.
    if os.path.exists("pwds.txt") == True:
        os.remove("pwds.txt")
        print(Fore.RED + "[ALERT] >>> " + Fore.YELLOW + "Passwords deleted!")
        exit()
    else:
        print(Fore.MAGENTA + "[CRTITCAL] >>> " + Fore.YELLOW +  "Password file does not exist")
        cont = input(Fore.RED + "[ALERT] >>> " + Fore.YELLOW + "Write password list? [y/n]: ")
        writePass()
        if cont == "n":
            read = input("Read password file? [y/n]: ")
            # Reading the file and printing it out.
            if read == "y":
                pwdfile = open("pwds.txt", "r")
                for z in pwdfile.read().split(","):
                    print(z)
            exit()
read = input("Read password file? [y/n]: ")
# Reading the file and printing it out.
if read == "y":
    pwdfile = open("pwds.txt", "r")
    for z in pwdfile.read().split(","):
        print(z)

cont = input(Fore.RED + "[ALERT] >>> " + Fore.YELLOW + "Write password list? [y/n]: ")
if cont == "y":
    writePass()
    exit("Complete")



pwdfile = open("pwds.txt", "w")
pwdfile.write("")
pwdfile.close() 
num = 50 # define the length of the string 
for f in range(5):
	print(Fore.MAGENTA + "[CRTITCAL] >>> " + Fore.YELLOW +  "Generating Secure Password!" + Fore.RESET)
	res = ''.join(secrets.choice(string.ascii_letters + string.digits + string.punctuation) for x in range(num))  
	# Print the Secure string with the combonation of letters, digits and punctuation   
	#print("Secure random string is :  "+ str(res))
	passw = []
	for i in res:
		if i in ["~", "{", "}", "*", "\\", "/", "//", "]", "[", "=", ":", ";", "|", "\"", "\,", "\'", "`"]:
			continue
		else:
			passw.append(i)
	print("Secure random string is:  " + ''.join(passw))
	pwdfile = open("pwds.txt", "a")
	pwdfile.write(''.join(passw) + "\n")
	pwdfile.close()