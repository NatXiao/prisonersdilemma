from Player import Player

class KindMajority(Player):
    def decide(self):
        if self.points:
            if sum(self.points)> len(self.points)/2:
                return True
            else :
                return False
        else :
            return True