from colorama import Fore

#This is a vein diagram calulator, you can add more values if you want
#Version: beta-1.0
#A easier more simple input will be coming soon!
#Soon maybe a while

def inputVal():
    overall = input("Total: ")
    a = input("Group A: ")
    b = input("Group B: ")
    none = input("Neither: ")
    abc = int(a)+int(b)+int(none) 
    both = int(abc)-int(overall)
    aOut = int(a)-int(both)
    bOut = int(b)-int(both)
    print(Fore.RED + "\n==================" + Fore.GREEN + "\nGroup A: " + str(aOut) + "\nGroup B: " + str(bOut) + "\nBoth: " + str(both) + "\nNone: " + str(none) + Fore.RED + "\n==================\n")

inputVal() 