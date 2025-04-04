from Player import Player
import random


class RandomPlayer(Player):
    def decide(self):
        return random.randint(0, 1)
