import time
import os
import json

def load_tasks():
    global tasks
    try:
        with open("saved_tasks.json", "r", encoding="utf-8") as file:
            tasks = json.load(file)
    except FileNotFoundError:
        tasks = []

def save_tasks():
            with open("saved_tasks.json", "w", encoding="utf-8") as file:
                json.dump(tasks, file, ensure_ascii=False, indent=4)

tasks = []
load_tasks()

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

        in_1_menu = True
        
        while in_1_menu:
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

    elif choise == "2":
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
            
                save_tasks()  # Save tasks after adding a new one

                os.system("cls")
                print(f"Successfully added: '{new_task}'")
                time.sleep(1)

            else:
                os.system("cls")
                print("\nWrong input!")
                time.sleep(0.5)
    
    elif choise == "3":
        os.system("cls")
        in_delete_menu = True
        while in_delete_menu:
            print("\nDelete menu: ")
            print("1. Back to menu")
            print("2. Delete task by number")
            
            delete_choise = input("\nType 1 to back to menu or 2 to delete task by number: ")

            if delete_choise == "1":
                os.system("cls")
                print("Back to menu...")
                time.sleep(1)
                in_delete_menu = False
            elif delete_choise == "2":
                    os.system("cls")
                
                    print("--# Delete task #--")
                
                    if len(tasks) == 0:
                        print("You have 0 tasks, nothing to delete!")
                        time.sleep(2)
                        os.system("cls")

                    else:
                        number = 1
                        for task in tasks:
                            print(f"{number}. {task}")
                            number += 1
            
                        try:
                            task_num = int(input("\nType task number what you need delete: "))
                            python_task_num = task_num - 1

                            if 0 <= python_task_num < len(tasks):
                                removed = tasks.pop(python_task_num)

                                save_tasks()  # Save tasks after deleting one

                                os.system("cls")
                                print(f"Successfully deleted: '{removed}'")
                                time.sleep(1)
                                os.system("cls")
                                    
                            else:
                                os.system("cls")
                                print("This task not found, type true number")
                                time.sleep(1.5)
                                os.system("cls")
                                
                        except ValueError:
                            os.system("cls")
                            print("Invalid input! Please type a number, not letters!")
                            time.sleep(1.5)
                            os.system("cls")
            else:
                os.system("cls")
                print("\nWrong input!")
                time.sleep(0.5)
                os.system("cls")
                    
    elif choise == "4":
        os.system("cls")

        print("\nGoodbye!")
        time.sleep(2)
        break