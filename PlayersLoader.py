import os
import importlib
import inspect
from Player import Player


def loadPlayerClass(folder="players"):
    players = {}
    for file in os.listdir(folder):
        if file.endswith(".py"):
            filetype = file[:-3]
            filepath = f"{folder}.{filetype}"

            module = importlib.import_module(filepath)

            for name, obj in inspect.getmembers(module, inspect.isclass):
                if issubclass(obj, Player) and name is not 'Player':
                    players[name] = obj
    return players