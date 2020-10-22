from art import *
from Conditions import *
import weakref



def main():

    #printing all instances
    for instance in Condition.instances:
        print(instance.name)

    #Checking for user input
    userEntry = input("Enter a condition:\n")
    x = userEntry.lower()
    userCondition = x.replace(" ", "_")
    print(userCondition)


    if userCondition in globals():
        print("true")
    else:
        print("false")

main()