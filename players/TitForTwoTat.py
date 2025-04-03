from players.Player import Player


class TitForTwoTat(Player):

    def decide(self, res: bool = True):
        if self.opponentsMove :
            if not self.opponentsMove[-1] and not self.opponentsMove[-2]:
                return False
        else :
            return True
