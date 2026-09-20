from abc import ABC, abstractmethod
from pathlib import Path
import os, sys

class HistopyBase(ABC):
    @property
    @abstractmethod
    def history_path(self) -> str:
        pass

    def _read_history(self) -> list[str]:
        path = Path(self.history_path).expanduser()

        if not path.exists():
            return []

        with path.open("r", encoding="utf-8", errors="ignore") as file:
            return [line.rstrip("\n") for line in file]

    def listall(self):
        commands = self._read_history()

        for index, command in enumerate(commands, start=1):
            print(f"{index}: {command}")

    def last(self):
        commands = self._read_history()

        if not commands:
            print("Nenhum comando no histórico.")
            return

        print(f"Last command: {commands[-1]}")

    def id(self):
        commands = self._read_history()

        for index, command in enumerate(commands, start=1):
            if index == int(sys.argv[2]):
                print(f"{index}: {command}")
                break
        else:
            print("Command not found.")


class WindowsHistopy(HistopyBase):
    @property
    def history_path(self) -> str:
        # Ajuste esse caminho para o shell que você usa no Windows
        return str(Path.home() / "AppData" / "Roaming" / "Microsoft" / "Windows" / "PowerShell" / "PSReadLine" / "ConsoleHost_history.txt")


class LinuxHistopy(HistopyBase):
    @property
    def history_path(self) -> str:
        # Ajuste se você usa zsh/fish/etc.
        return str(Path.home() / ".bash_history")

def create_histopy_instance() -> HistopyBase:
    if os.name == "nt":
        return WindowsHistopy()
    return LinuxHistopy()