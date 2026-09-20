import os, sys
from histopyBASEclass import create_histopy_instance
from pathlib import Path

histopy = create_histopy_instance()

if __name__ == "__main__":

    if len(sys.argv) == 1:
        print(
            "Usage: python histopy.py [listall|last|id]\n"
            "listall: List all commands in the history.\n"
            "last: Show the last command in the history.\n"
            "id: List especific command in the history."
        )
    elif len(sys.argv) > 3:
        raise Exception("Invalid number of arguments provided.")
    else:
        if sys.argv[1] == "listall":
            histopy.listall()
        elif sys.argv[1] == "last":
            histopy.last()
        elif sys.argv[1] == "id":
            histopy.id()
        else:
            raise Exception("Invalid argument provided.")