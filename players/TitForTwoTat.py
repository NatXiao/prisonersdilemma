from Player import Player


class TitForTwoTat(Player):

    def decide(self):
        if self.opponentsMove:
            if not self.opponentsMove[-1] and not self.opponentsMove[-2]:
                return False
        else:
            return True
