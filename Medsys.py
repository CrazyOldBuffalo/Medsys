from art import *

#Used to import the Conditions class and all objects into main()
from Conditions import *

#Used for listing all created objects in the class
import weakref

#Basic Function to List the menu at Launch
def menu():
    line =  60 * "*";
    print(line.center(80))
    print("*".center(21) + "MedSys".center(40) + "*".center(18))
    print("*".center(21) + "Version 1.0 - © Tomasz Boberek 2020".center(45) + "*".center(8))
    print(line.center(80))
    menuloop = True;
    while (menuloop == True):
        print("*".center(21) + "Menu: ".center(40) + "*".center(18))
        print(line.center(80))
        print("*".center(21) + "1:                         List Conditions" + "*".center(14))
        print("*".center(21) + "2:                       Search Conditions" + "*".center(14))
        print("*".center(21) + "3:                      N/I Add Conditions" + "*".center(14))
        print("*".center(21) + "4:                                    Quit" + "*".center(14))   
        print(line.center(80))
        #Input data validation, Checks for empty or string values and catches errors
        #Valid input launches corresponding function
        try:
            menuinp = int(input("Please Input your choice:  \n"))
            if (menuinp == 1):
                menuloop = False
                print("Listing conditions")
                listing()
            elif (menuinp == 2):
                menuloop = False
                print("Searching")
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
        except TypeError:
            print("Incorrect Input try again")
        
def listing():
    for instance in Condition.instances:
        print(instance.name)
    print("Hello")           

                




def main():
    menu()
    #printing all instances
    #Checking for user input
    userEntry = input("Enter a condition:\n")
    userEntry = userEntry.lower()
    if " " in userEntry:
        userCondition = userEntry.replace(" ", "_")
    print(userCondition)


    if userCondition in globals():
        print("true")
    else:
        print("false")

main()

