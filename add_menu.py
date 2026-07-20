from load_save_tasks import save_tasks
from refresh_list import refresh_list
import os
import time

def add_menu():
    tasks = refresh_list()
    os.system("cls")
    in_add_menu = True
    while in_add_menu:
        os.system("cls")
        print("\nAdd menu: ")
        print("1. Back to menu")
        print("2. Add task to list")

        add_choise = input("\nType 1 to back to menu or 2 to add task: ")

        if add_choise == "1":
            os.system("cls")
            print("Back to menu...")
            time.sleep(1)
            in_add_menu = False
        elif add_choise == "2":
            os.system("cls")
            print("--# Add task #--")
            new_task = input("Type the task to see it in list: ")
            tasks.append(new_task)

            save_tasks(tasks)
            
            os.system("cls")
            print(f"Successfully added: '{new_task}'")
            time.sleep(1)

        else:
            os.system("cls")
            print("\nWrong input!")
            time.sleep(0.5)