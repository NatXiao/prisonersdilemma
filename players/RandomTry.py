from players.Player import Player
import random


class RandomTry(Player):

    def decide(self, res: bool = True):
        return self.opponentsMove[-1] if self.opponentsMove else True
