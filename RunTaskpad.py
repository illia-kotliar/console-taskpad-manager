from load_save_tasks import load_tasks, save_tasks
from delete_menu import delete_menu
from add_menu import add_menu
from view_menu import view_menu
import time
import os

tasks = load_tasks()

while True:
    os.system("cls")

    print("     ")
    print("--# Taskbar menu #--")
    print("1. See your tasks")
    print("2. Add tasks to taskbar")
    print("3. Remove tasks from taskbar")
    print("4. Exit")
    print("     ")

    choise = input("Choise what you want(type 1,2,3 or 4): ")

    if  choise == "1":
        view_menu()

    elif choise == "2":
        add_menu()
    
    elif choise == "3":
        delete_menu()
                   
    elif choise == "4":
        os.system("cls")

        print("\nGoodbye!")
        time.sleep(2)
        break
