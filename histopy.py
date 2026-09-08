import os, sys, win, linux
from pathlib import Path

def get_os():
    usr_os = os.name
    if usr_os == 'nt':
        return win
    elif usr_os == 'linux':
        return linux
    else:
        raise Exception("Unsupported operating system: {}".format(usr_os))

if __name__ == "__main__":
    if len(sys.argv) > 2 or len(sys.argv) < 2:
        raise Exception("Invalid number of arguments provided. Please provide exactly one argument.")
    else:
        os_module = get_os()
        if sys.argv[1] == "getall":
            os_module.getall()
        elif sys.argv[1] == "getlast":
            os_module.getlast()
        else:
            raise Exception("Invalid argument provided.")