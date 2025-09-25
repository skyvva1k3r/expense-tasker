import time
from datetime import datetime
import os
import sys

l = []
obj = ["id", "description", "amount", "date"]
month = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

def menu():
    print("\n1. Add waste.\n2. List wastes\n3. Delete waste.\n4. Update waste.\n5. Finally leave.\n")
    n = input()
    try:
        n = int(n)
    except ValueError:
        os.system('cls')
        print("\nThats not a num, you prick.\n")
        return 0
    match n:
        case 1:
            os.system('cls')
            add_waste()
        case 2:
            os.system('cls')
            list_waste()
        case 3:
            os.system('cls')
            delete_waste()
        case 4:
            os.system('cls')
            update_waste()
        case 5:
            sys.exit()
        case _:
            os.system('cls')
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
    overall = 0
    if len(l) == 0:
        os.system('cls')
        print("\nNo wastes for now.\n\n")
        return 0
    match len(n):
        case 1:
            for waste in l:
                overall += waste[2]
                for attr in waste:
                    print(f"{obj[waste.index(attr)]} -> {attr}")
                print(f"\nOverall sum for all is {overall}")    
            print()
        case 2:
            for waste in l:
                if waste[3][:2] == n:
                    overall += waste[2]
                    counter += 1
                    for attr in waste:
                        print(f"{obj[waste.index(attr)]} -> {attr}")
                print(f"\nOverall sum for period is {overall}")
            print()
        case 4:
            for waste in l:
                if waste[3][6:] ==n:
                    overall += waste[2]
                    counter += 1
                    for attr in waste:
                        print(f"{obj[waste.index(attr)]} -> {attr}")    
                print(f"\nOverall sum for period is {overall}")
            print()
        case _:
            print("Something went wrong.\n")
            return 0
    if counter == 0 and len(n) != 1:
        print("\nNothing found.\n")
    print()

def delete_waste():
    if len(l) == 0:
        print("No tasks at all.")
        return 0
    print("Enter id of waste you want to delete:\n")
    n = input()
    try:
        n = int(n)
    except ValueError:
        os.system('cls')
        print("Thats not id.\n")
        return 0
    if n > len(l):
        print("Given id is out of range.\n")
        return 0
    l.pop(n-1)
    for i in range(n - 1, len(l), 1):
        l[i][0] -= 1

def update_waste():
    if len(l) == 0:
        print("No tasks at all.")
        return 0
    print("Enter id of waste you want to update:\n")
    n = input()
    try:
        n = int(n)
    except ValueError:
        os.system('cls')
        print("Thats not id.\n")
        return 0
    if n > len(l):
        print("Given id is out of range.\n")
        return 0
    print("\nWhat do you want to change?\n1. Description.\n2. Amount.\n3. Date.\n")
    m = input()
    try:
        m = int(m)
    except ValueError:
        os.system('cls')
        print("Thats not a variant.\n")
        return 0
    for waste in l:
        if waste[0] == n:
            match m:
                case 1:
                    waste[1] = input("\nEnter new description.\n")
                case 2:
                    amount = input("\nEnter new amount:\n")
                    try:
                        amount = int(amount)
                    except ValueError:
                        os.system('cls')
                        print("Thats not an amount.\n")
                        return 0
                    waste[2] = amount
                case 3:
                    tempStr = input("Enter a date (YYYY-MM-DD):\n")
                    try: 
                        tempStr = datetime.strptime(tempStr, "%Y-%m-%d")
                    except ValueError:
                        os.system('cls')
                        print("\nWrong time format, try again.")
                        return 0
                    tempStr = datetime.strftime(tempStr, "%m-%d-%Y")
                    waste[3] = tempStr

while True:
    menu()