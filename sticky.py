import sys
import getter

# getter.get_note()
# exit()

if len(sys.argv) == 1:
    while True:
        instruction = input("How can I help you?\n1. View a note (type 'view')\n2. Add a note (type 'add')\nResponse : ")
        if instruction not in ["view","add"]:
            print("invalid choice!")
        else:
            break
    if instruction == "view":
        pass

inputs = sys.argv[:2]

# Row column Indexing
# Editing ROws in Pandas DF "inplace"
# argparse
