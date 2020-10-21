from art import *
from Conditions import *



def main():

    #Checking for user input
    usercondition = input("Enter a condition:\n")
    
    if usercondition in globals():
        print("true")
    else:
        print("false")

main()