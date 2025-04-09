from Player import Player

class KindMajority(Player):
    def decide(self):
        if self.opponentsMove:
            if sum(self.opponentsMove)> len(self.opponentsMove)/2:
                return True
            else :
                return False
        return True