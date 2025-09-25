import time
from datetime import datetime
import os
import sys
import click

l = []
obj = ["id", "description", "amount", "date"]
month = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

@click.group()
def cli():
    """Manage your money spending with this app."""
    loaded = load()
    if loaded > 0:
        click.echo(f"\nLoaded {loaded} tasks")
    pass

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
            save()
            sys.exit()
        case _:
            os.system('cls')
            print("bruh, wrong action. Try again.\n")
            return 0
        
def save():
    file = open('data.txt', 'w')
    file.write(str(len(l)))
    file.write("\n")
    for waste in l:
        temp = []
        for attr in waste:
            temp.append(str(attr))
        file.write("|".join(temp))
        file.write("\n")
    file.close()

def load():
    try:
        file = open('data.txt', 'r')
    except FileNotFoundError:
        return 0
    try:
        n = int(file.readline())
    except ValueError:
        return 0
    if n == 0:
        return 0
    for i in range(n):
        temp = (file.readline()).split("|")
        temp[-1] = temp[-1][:-1]
        temp[0], temp[2] = int(temp[0]), int(temp[2])
        l.append(temp)
        temp = []
    return n

@cli.command()
@click.option('--description', prompt = '\nDescription of spending', help = 'Description of spending.')
@click.option('--amount', prompt = '\nAmount of spending', help='Amount of spending.')
@click.option('--date', prompt = '\nDate (YYYY-MM-DD)', help='Date (YYYY-MM-DD).')
def add(description, amount, date):
    if add_waste(description, amount, date) == 1:
        click.echo(f"\nAll great.")
    else:
        click.echo(f"\nShit happens.")

def add_waste(description, amount, date):
    temp = []
    for i in range(len(obj)):
        match i:
            case 0:
                temp.append(len(l)+1)
            case 1:
                temp.append(description)
            case 2:
                try:
                    amount = int(amount)
                except ValueError:
                    os.system('cls')
                    print("\nThats not an amount.")
                    return 0
                amount = int(amount)
                temp.append(amount)
            case 3:
                try: 
                    date = datetime.strptime(date, "%Y-%m-%d")
                except ValueError:
                    os.system('cls')
                    print("\nWrong time format, try again.")
                    return 0
                date = datetime.strftime(date, "%m-%d-%Y")
                temp.append(date)
    l.append(temp)
    save()
    return 1

@cli.command()
@click.option('--type', prompt="\n'0' for all, 'MM' for month sort, 'YYYY' for year sort", help='Show all spendings.')
def list(type):
    if list_waste(type) == 1:
        click.echo(f"\nAll great.")
    else:
        click.echo(f"\nShit happens.")    

def list_waste(type):
    counter = 0
    overall = 0
    if len(l) == 0:
        os.system('cls')
        print("\nNo wastes for now.")
        return 0
    print()
    match len(type):
        case 1:
            for waste in l:
                overall += waste[2]
                for attr in waste:
                    print(f"{obj[waste.index(attr)]} -> {attr}")
                print()
            print(f"\nOverall sum for all is {overall}")    
            print()
        case 2:
            for waste in l:
                if waste[3][:2] == type:
                    overall += waste[2]
                    counter += 1
                    for attr in waste:
                        print(f"{obj[waste.index(attr)]} -> {attr}")
                    print()
            print(f"\nOverall sum for period is {overall}")
            print()
        case 4:
            for waste in l:
                if waste[3][6:] ==type:
                    overall += waste[2]
                    counter += 1
                    for attr in waste:
                        print(f"{obj[waste.index(attr)]} -> {attr}")
                    print()    
            print(f"\nOverall sum for period is {overall}")
            print()
        case _:
            return 0
    if counter == 0 and len(type) != 1:
        print("\nNothing found.")
    print()
    return 1

@cli.command()
@click.option('--id', prompt='\nid of the spending', help= 'id of the spending.')
def delete(id):
    if delete_waste(id) == 1:
        click.echo(f"\nAll great.")
    else:
        click.echo(f"\nShit happens.")

def delete_waste(id):
    if len(l) == 0:
        print("\nNo tasks at all.")
        return 0
    try:
        id = int(id)
    except ValueError:
        os.system('cls')
        print("\nThats not id.")
        return 0
    if id > len(l):
        print("\nGiven id is out of range.")
        return 0
    l.pop(id-1)
    for i in range(id - 1, len(l), 1):
        l[i][0] -= 1
    save()
    return 1

@cli.command()
@click.option('--id', prompt='\nid of the spending', help= 'id of the spending.')
@click.option('--type', prompt='\nWhat do you want to change?\n1. Description.\n2. Amount.\n3. Date.\n', help='Type of data to change.')
@click.option('--changes', prompt='\nEnter final version.', help ='New data.')
def update(id, type, changes):
    if update_waste(id, type, changes) == 1:
        click.echo(f"\nAll great.")
    else:
        click.echo(f"\nShit happens.")

def update_waste(id, type, changes):
    if len(l) == 0:
        print("\nNo tasks at all.")
        return 0
    print("Enter id of waste you want to update:")
    try:
        id = int(id)
    except ValueError:
        os.system('cls')
        print("Thats not id.")
        return 0
    if id > len(l):
        print("Given id is out of range.")
        return 0
    try:
        type = int(type)
    except ValueError:
        os.system('cls')
        print("Thats not a variant.")
        return 0
    for waste in l:
        if waste[0] == id:
            match type:
                case 1:
                    waste[1] = changes
                case 2:
                    try:
                        changes = int(changes)
                    except ValueError:
                        os.system('cls')
                        print("Thats not an amount.")
                        return 0
                    waste[2] = changes
                case 3:
                    changes = input("Enter a date (YYYY-MM-DD):")
                    try: 
                        changes = datetime.strptime(changes, "%Y-%m-%d")
                    except ValueError:
                        os.system('cls')
                        print("\nWrong time format, try again.")
                        return 0
                    changes = datetime.strftime(changes, "%m-%d-%Y")
                    waste[3] = changes
    save()
    return 1

if __name__ == "__main__":
    cli()