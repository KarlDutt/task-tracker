#commit on nagu save, kui on mingi uus asi juurde lisatud, nt uus function
#push = kõik tehtud, pane serverile
import sys
import json
import os
import uuid

FILENAME = "biglist.json"

#read json or create new if there's none
if os.path.exists(FILENAME):
    with open(FILENAME, "r", encoding="utf-8") as file:
        items_list = json.load(file)
else:
    items_list = []

#add an item to list
def add():
    if len(sys.argv) >= 2 and sys.argv[1] == "add":
        items_list.append(sys.argv[2])

add()

#save new list to json
with open("biglist.json", mode="w", encoding="utf-8") as write_file:
    json.dump(items_list, write_file)

