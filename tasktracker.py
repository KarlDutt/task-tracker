import sys
import json
import os
import uuid
from datetime import datetime

FILENAME = "biglist.json"
def now_time():
    return datetime.now().isoformat()
#read json or create new if there's none
if os.path.exists(FILENAME) and os.path.getsize(FILENAME) > 0:
    with open(FILENAME, "r", encoding="utf-8") as file:
        items_list = json.load(file)
else:
    items_list = []

#add an item to list
#tasktracker.py add "description"
def add():
    if len(sys.argv) >= 3 and sys.argv[1] == "add":

        task = {
            "id": str(uuid.uuid1()),
            "description": sys.argv[2],
            "status": 0, #0=incomplete, 1= in progress, 2= completed
            "createdAt": now_time(),
            "updatedAt": now_time()
        }
        items_list.append(task)
    else:
        print("wrong command, didn't write description")

#tasktracker.py delete "description"
def delete():
    if len(sys.argv) >= 3 and sys.argv[1] == "delete":
        for i, task in enumerate(items_list):
            if sys.argv[2] == task["description"]:
                items_list.remove(task)
                print(f"{task['description']} removed from list")
                return
            if sys.argv[2] == task["id"]:
                items_list.remove(task)
                print(f"{task['id']} removed from list")
                return
        else:
            print("sorry no such task")





#show all the tasks. only the description and status
#tasktracker.py list "done" / "all"
def list_tasks():
    if len(sys.argv) >= 3 and sys.argv[1] == "list" and sys.argv[2] in ["all", "done", "in progress", "not done"]:
        filter_status = sys.argv[2]
        enumerate_status(filter_status)
    else:
        print("wrong command")
        

def enumerate_status(filter_status):
    for i, task in enumerate(items_list, start=1):
        status_str = ""
                #1. watch tv. not done
        if  task["status"] == 0:
            status_str = "not done"

        elif task["status"] == 1:
            status_str = "in progress"

        elif task["status"] == 2:
            status_str = "done"
        else:
            print("status is unknown")

        if filter_status == "all" or status_str == filter_status:
            print(f"{i}. {task['description']} - {status_str}")


#tasktracker.py update "watch tv" "completed" / to "watch tv later"
def update_task():
    if len(sys.argv) >= 4 and sys.argv[1] == "update":
        updated = False
        for task in items_list:
            if task["description"] == sys.argv[2]:
                updated = False
                #change status
                if sys.argv[3] == "completed":
                    task["status"] = 2
                    updated = True
                elif sys.argv[3] == "in progress":
                    task["status"] = 1
                    updated = True

                #change name
                elif sys.argv[3] == "to":
                        task["description"] = sys.argv[4]
                        updated = True
                if updated:
                     task["updatedAt"] = now_time()
                     print("task updated") 


def main():
    if len(sys.argv) < 2:
        print("no command provided. use list, update, add or remove")
        return
    
    command = sys.argv[1]

    if command == "add":
        add()
    elif command == "update":
        update_task()
    elif command == "list":
        list_tasks()
    elif command == "delete":
        delete()
    else:
        print("unknown command, use list, update, add or remove")

    #save new list to json
    with open("biglist.json", mode="w", encoding="utf-8") as write_file:
        json.dump(items_list, write_file, indent=4)


if __name__ == "__main__":
    main()

