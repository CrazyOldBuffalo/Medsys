from Conditions import *
import json
import pprint
#Basic Function to List the menu at Launch
def menu():
    line =  41 * "*";
    print(line.center(40))
    print("*" + "MedSys".center(35) + "*".center(9))
    print("*" + "  Version 1.0 - © Tomasz Boberek 2020  ".center(30) + "*")
    print(line.center(40))
    menuloop = True;
    while (menuloop == True):
        print("*" + "Menu: ".center(39) + "*")
        print(line.center(40))
        print("*" + " 1:                    List Conditions " + "*")
        print("*" + " 2:                  Search Conditions " + "*")
        print("*" + " 3:                 N/I Add Conditions " + "*")
        print("*" + " 4:                               Quit " + "*")   
        print(line.center(40))
        #Input data validation, Checks for empty or string values and catches errors
        #Valid input launches corresponding function
        try:
            menuinp = int(input("*" + " Please Input your choice:           "))
            if (menuinp == 1):
                menuloop = False
                print("Listing conditions".center(80))
                listing()
            elif (menuinp == 2):
                menuloop = False
                print("Searching")
                search()
            elif (menuinp == 3):
                menuloop = False
                print("Adding Conditions, Not Implemented")
            elif (menuinp == 4):
                menuloop = False
                exit(0)
            else:
                print("Please Enter a value between 1 & 4")
        except ValueError:
            print("Incorrect Input try again")
        
def listing():
    line = 41 * "*"
    print(line.center(40))
    print(*allconditions.keys(), sep="\n")
    
def printing(name):   
    print(json.dumps(allconditions[name], indent=2))

def search():
    line = 41 * "*"
    print(line.center(40))
    name = input("*" + "Enter a Condition \n").title()
    if name in allconditions:
        printing(name)
    else:
        print("Not in Current Database")

def main():
    menu()

main()

