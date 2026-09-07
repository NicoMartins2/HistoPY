import os
from pathlib import Path

history_dir = Path.home() / 'AppData' / 'Roaming' / 'Microsoft' / 'Windows' / 'PowerShell' / 'PSReadLine' / 'ConsoleHost_history.txt'

with open(history_dir, 'r', encoding='utf-8') as file:
    history = file.readlines()
    print("".join(history))