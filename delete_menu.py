from load_save_tasks import save_tasks
from refresh_list import refresh_list
import os
import time


def delete_menu():
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
            tasks = refresh_list()
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

                        save_tasks(tasks)  # Save tasks after deleting one

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