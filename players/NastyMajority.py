from Player import Player

class NastyMajority(Player):
    def decide(self):
        if self.opponentsMove:
            if sum(self.opponentsMove)> len(self.opponentsMove)/2:
                return False
            else :
                return True
        return False