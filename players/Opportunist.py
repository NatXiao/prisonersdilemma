from Player import Player


class Opportunist(Player):

    def decide(self):
        if self.points:
            if self.points[-1] > 1:
                return False
            else:
                return True
        return False
