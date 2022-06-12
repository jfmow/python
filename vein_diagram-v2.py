from colorama import Fore

#This is a vein diagram calulator, you can add more values if you want
#Version: beta-1.0
#A easier more simple input will be coming soon!

def inputVal():
    overall = input("Total: ")
    a = input("Group A: ")
    b = input("Group B: ")
    none = input("Neither: ")
    abc = int(a)+int(b)+int(none)
    more = input("Do you require more groups? [y/n]: ")
    if more == "y" or "Y":
        # Asking the user how many values they want to add, then it is asking the user to input the
        # values.
        ammount = int(input("How many: "))
        vals = []
        # Asking the user how many values they want to add, then it is asking the user to input the
        # values.
        for i in range(ammount):
            vals.append(int(input("value: ")))
        # Adding the values of the list together.
        valssum = sum(vals)
        # Adding the values of the list together.
        abc_val_sum = int(abc)+int(valssum)
        #Working ⬆⬆
        print(abc_val_sum)
        both = int(abc_val_sum)-int(overall)
        aOut = int(a)-int(both)
        bOut = int(b)-int(both)
        #DO vals in array out for groups

        print(Fore.RED + "\n==================" + Fore.GREEN + "\nGroup A: " + str(aOut) + "\nGroup B: " + str(bOut) + "\nBoth: " + str(both) + "\nNone: " + str(none) + Fore.RED + "\n==================\n")


    else:
        both = int(abc)-int(overall)
        aOut = int(a)-int(both)
        bOut = int(b)-int(both)
        print(Fore.RED + "\n==================" + Fore.GREEN + "\nGroup A: " + str(aOut) + "\nGroup B: " + str(bOut) + "\nBoth: " + str(both) + "\nNone: " + str(none) + Fore.RED + "\n==================\n")

#inputVal() 
print(Fore.RED + "=======================================\n" + "               !ALERT!\n" + " This program is currently unavailable" + "\n=======================================")