import os, sys, win, linux
from pathlib import Path

def get_os():
    usr_os = os.name
    if usr_os == 'nt':
        history_dir = Path.home() / 'AppData' / 'Roaming' / 'Microsoft' / 'Windows' / 'PowerShell' / 'PSReadLine' / 'ConsoleHost_history.txt'
        if not history_dir.exists():
            Path.mkdir(history_dir, parents=True) # create the directory if it doesn't exist
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
        if sys.argv[1] == "all":
            os_module.all()
        elif sys.argv[1] == "last":
            os_module.last()
        elif sys.argv[1] == "id":
            os_module.id()
        else:
            raise Exception("Invalid argument provided.")