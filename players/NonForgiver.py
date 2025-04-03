from players.Player import Player


class NonForgiver(Player):

    def decide(self, res: bool = True):
        return not (False in self.opponentsMove) 
