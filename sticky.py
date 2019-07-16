import sys
import getter
import adder


# getter.get_note()
# exit()
print("Enter password: ")
count = 5
while True:
    password = input()
    if password == "sticky":
        break
    else:
        print("try again")
        count = count-1
    if count == 0:
        print("max chances given")
        exit()


if len(sys.argv) == 1:
    while True:
        instruction = input("How can I help you?\n1. View a note (type 'view')\n2. Add a note (type 'add')\nResponse : ")
        if instruction not in ["view","add"]:
            print("invalid choice!")
        else:
            break
    if instruction == "view":
        num = input("Note you want to see: ")
        getter.get_note(num)
    elif instruction == "add":
        note_heading = input("please enter the heading of the note: \n")
        note_main = input("enter note:")
        adder.add_note(note_heading,note_main)
inputs = sys.argv[:2]

# Row column Indexing
# Editing ROws in Pandas DF "inplace"
# argparse
