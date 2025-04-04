from Player import Player
import random


class RandomTry(Player):

    def decide(self):
        if 10 > random.random():
            return False
        else:
            return True
