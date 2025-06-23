#commit on nagu save, kui on mingi uus asi juurde lisatud, nt uus function
#push = kõik tehtud, pane serverile
import sys
print(sys.argv)

biglist = []

def add():
    if len(sys.argv) >= 2 and sys.argv[1] == "add":
        biglist.append(sys.argv[2])

add()
print(biglist)