from players.Player import Player


class TitForTat(Player):

    def decide(self):
        return self.opponentsMove[-1] if self.opponentsMove else True
