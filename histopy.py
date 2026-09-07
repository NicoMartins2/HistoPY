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
    if len(sys.argv) > 2:
        raise Exception("Too many arguments provided. Please provide only one argument.")