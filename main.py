import time
from datetime import datetime
import os

print("Thats crazy awful expense tasker to count your hard waste of money biatch.\n")

def menu():
    print("Here you are. Pick your action:\n")
    print("1. Add waste.\n2. List wastes\n3. Delete waste.\n4. Finally leave.")
    n = input()
    try:
        n = int(n)
    except ValueError:
        print("\nThats not a num, you prick.\n")
        return 0
    match n:
        case 1:
            return 0
    

while True:
    menu()