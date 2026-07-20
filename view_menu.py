from refresh_list import refresh_list
import os
import time

def view_menu():
    in_1_menu = True
        
    while in_1_menu:
        tasks = refresh_list()
        os.system("cls")
        print("     ")
        print("--# Tasks list #--")
        
        if len(tasks) == 0:
            print("You have 0 tasks, please add minimum 1 task")
        else:
            for task in tasks:
                print("-" + task)
        print("\nView menu:")
        print("1. Back to menu")

        view_choise = input("\nType 1 to back to menu: ")

        if view_choise == "1":
            os.system("cls")
            print("Back to menu...")
            time.sleep(1)
            in_1_menu = False
        else:
            os.system("cls")
            print("This choise not found, please type 1 to back to menu")
            time.sleep(2)
            os.system("cls")