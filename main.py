import time
from datetime import datetime
import os
import sys

l = []
obj = ["id", "description", "amount", "date"]
month = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

def menu():
    print("\n1. Add waste.\n2. List wastes\n3. Delete waste.\n4. Finally leave.\n")
    n = input()
    try:
        n = int(n)
    except ValueError:
        os.system('cls')
        print("\nThats not a num, you prick.\n")
        return 0
    match n:
        case 1:
            add_waste()
        case 2:
            list_waste()
        case 4:
            sys.exit()
        case _:
            print("bruh, wrong action. Try again.\n")
            return 0

def add_waste():
    temp = []
    for i in range(len(obj)):
        match i:
            case 0:
                temp.append(len(l)+1)
            case 1:
                temp.append(input("\nType a description of waste:\n"))
            case 2:
                amount = input("Input amount of your waste:\n")
                try:
                    amount = int(amount)
                except ValueError:
                    os.system('cls')
                    print("Thats not an amount.\n")
                    return 0
                amount = int(amount)
                temp.append(amount)
            case 3:
                tempStr = input("Enter a date (YYYY-MM-DD):\n")
                try: 
                    tempStr = datetime.strptime(tempStr, "%Y-%m-%d")
                except ValueError:
                    os.system('cls')
                    print("\nWrong time format, try again.")
                    return 0
                tempStr = datetime.strftime(tempStr, "%m-%d-%Y")

                temp.append(tempStr)
    l.append(temp)

def list_waste():
    print("\nHow do you want to list your wastes?\n 'YYYY' to sort by year.\n 'MM' to sort by month.\n '0' to print all.\n")
    n = input()
    counter = 0
    if len(l) == 0:
        os.system('cls')
        print("\nNo wastes for now.\n\n")
        return 0
    match len(n):
        case 1:
            for waste in l:
                print()
                for attr in waste:
                    print(f"{obj[waste.index(attr)]} -> {attr}")        
        case 2:
            for waste in l:
                if waste[3][:2] == n:
                    counter += 1
                    for attr in waste:
                        print(f"{obj[waste.index(attr)]} -> {attr}")
        case 4:
            for waste in l:
                if waste[3][6:] ==n:
                    counter += 1
                    for attr in waste:
                        print(f"{obj[waste.index(attr)]} -> {attr}")    
        case _:
            print("Something went wrong.\n")
            return 0
    if counter == 0 and len(n) != 1:
        print("\nNothing found.\n")
    print()


while True:
    menu()