import os
from pathlib import Path

history_dir = Path.home() / 'AppData' / 'Roaming' / 'Microsoft' / 'Windows' / 'PowerShell' / 'PSReadLine' / 'ConsoleHost_history.txt'

def all():
    with open(history_dir, 'r', encoding='utf-8') as file:
        history = file.readlines()
        command_line_number = 0
        for i in range(len(history)):
            command_line_number += 1
            command = history[i].strip()
            print(f"{command_line_number}: {command}")

def last():
    with open(history_dir, 'r', encoding='utf-8') as file:
        history = file.readlines()
        last_command = history[-1].strip()
        print(f"Last command: {last_command}")

def id():
    with open(history_dir, 'r', encoding='utf-8') as file:
        history = file.readlines()
        command_line_number = 0
        for i in range(len(history)):
            command_line_number += 1
            command = history[i].strip()
            print(f"{command_line_number}: {command}")