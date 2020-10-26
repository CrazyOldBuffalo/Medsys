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
        print("*" + " 3:                     Add Conditions " + "*")
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
                Entry()
            elif (menuinp == 4):
                menuloop = False
                exit(0)
            else:
                print("Please Enter a value between 1 & 4")
        except ValueError:
            print("Incorrect Input try again")

def Entry():
    print("Creating new Entry: ")
    idloop = True
    while idloop == True:
        ID = str(input("Enter Identifier for Condition: \n"+ "NO NUMBERS OR SPACES \n")).lower()
        if len(ID) < 5:
            print("Please Enter a longer Identifier")
        elif " " in ID:
            print("No Spaces Please!")
        elif any(i.isdigit() for i in ID):
            print("No Numbers Please!")
        else:
            idloop = False
            print("Your Condition ID is: " + ID)
    nameloop = True
    while nameloop == True:
        nameinput = str(input("Enter Condition Name: \n"))
        nameinput = nameinput.title()
        print(nameinput)
        if len(nameinput) < 2:
            print("Thats Not Valid")
        else:
            nameloop = False
    descriptionloop = True
    while descriptionloop == True:
        descinput = str(input("Enter Condition Description: \n"))
        if len(descinput) < 5:
            print("That's too Short! Add more info")
        else:
            descriptionloop = False
    symptomloop = True
    while symptomloop == True:
        sympinput = str(input("Enter A Symptoms: \n"))
        if len(sympinput) < 5:
            print("Too Short add more!")
        else: 
            symptomloop = False
    treatloop = True
    while treatloop == True:
        treatinput = str(input("Enter Some Treatments: \n"))
        if len(treatinput) < 5:
            print("Too Short add more!")
        else:
            treatloop = False
    
    ID = dict(name = nameinput , description = descinput, symptoms = sympinput, treatment = treatinput)
    print("Record Added Successfully! \n")
    print(json.dumps(ID, indent = 2))
    entryloop = True
    while entryloop == True:
        entryin = input("Enter a New Record?  Y/N \n").upper()
        if entryin == "Y":
            entryloop = False
            Entry()
        elif entryin == "N":
            entryloop = False
            print("Returning to Menu!")
            menu()
        else:
            print("Not A valid input!")

    

        
def listing():
    line = 41 * "*"
    print(line.center(40))
    print(*allconditions.keys(), sep="\n")
    listingloop = True
    while listingloop == True:
        inlist = str(input("\n" + "List again?  Y/N \n")).upper()
        if inlist == "Y":
            listingloop = False
            listing()
        elif inlist == "N":
            listingloop = False
            print("Returning to Menu")
            menu()
        else:
            print("Please Enter Y/N")
    
def printing(name):   
    print(json.dumps(allconditions[name], indent=2 ))
    againloop = True
    while againloop == True:
        inagain = str(input("\n" + "Search Again? \n")).upper()
        if inagain == "Y":
            againloop = False
            search()
        elif inagain == "N":
            againloop = False
            print("Returning to Menu")
            menu()
        else:
            print("Please Enter Y/N")


def search():
    line = 41 * "*"
    print(line.center(40))
    name = input("*" + "Enter a Condition \n").title()
    if name in allconditions:
           printing(name)
    else:  
        print("Not in Current Database")
        researchloop = True
        while researchloop == True:
            research = input("Search Again?  Y/N \n").upper()
            if len(research) > 1:
                print("Please enter a Y/N")
            elif research == "Y":
                print("Searching again")
                researchloop = False
                search()
            elif research == "N":
                print("Returning to Menu")
                researchloop = False
                menu()
            else:
                print("Not a valid input")
def main():
    menu()

main()

