from Player import Player


class NonForgiver(Player):

    def decide(self):
        return not (False in self.opponentsMove)
