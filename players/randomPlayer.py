from players.Player import Player
import random


class RandomPlayer(Player):
    def decide(self, res: bool = True):
        return random.randint(0, 1)
