import sys
import json
import os
import uuid
from datetime import datetime

FILENAME = "biglist.json"
current_time = datetime.now().isoformat()

#read json or create new if there's none
if os.path.exists(FILENAME) and os.path.getsize(FILENAME) > 0:
    with open(FILENAME, "r", encoding="utf-8") as file:
        items_list = json.load(file)
else:
    items_list = []

#add an item to list
def add():
    if len(sys.argv) >= 2 and sys.argv[1] == "add":

        task = {
            "id": str(uuid.uuid1()),
            "description": sys.argv[2],
            "status": 0, #0=incomplete, 1= in progress, 2= completed
            "createdAt": current_time,
            "updatedAt": current_time
        }
        items_list.append(task)


#show all the tasks. only the description and status
def list_tasks():
    if len(sys.argv) >= 2 and sys.argv[1] == "list":
            for i, task in enumerate(items_list, start=1):
                status_str = ""
                #1. watch tv. not done
                print(f"{i}. {task['description']}")

                if  task["status"] == str(0):
                    status_str = "not done"

                elif task["status"] == str(1):
                    status_str = "in progress"

                elif task["status"] == str(2):
                    status_str = "done"
                else:
                    print("status is unknown")

                print(status_str)

#update using description
#can update task name. can update status. always needs to add updatedAt
#tasktracker.py update "watch tv" "completed" / to "watch tv later"
def update_task():
    if len(sys.argv) >= 4 and sys.argv[1] == "update":
        updated = False
        for task in items_list:
            if task["description"] == sys.argv[2]:
                updated = False
                if sys.argv[3] == "completed":
                    task["status"] = 2
                    updated = True
                elif sys.argv[3] == "in progress":
                    task["status"] = 1
                    updated = True
                elif sys.argv[3] == "to":
                        task["description"] = sys.argv[4]
                        updated = True
                if updated:
                     task["updatedAt"] = datetime.now().isoformat()
                     print("task updated") 

add()
list_tasks()
update_task()
#save new list to json
with open("biglist.json", mode="w", encoding="utf-8") as write_file:
    json.dump(items_list, write_file, indent=4)