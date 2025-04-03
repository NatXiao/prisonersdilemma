from Player import Player

class NastyMajority(Player):
    def decide(self):
        if self.points:
            if sum(self.points)> len(self.points)/2:
                return False
            else :
                return True
        else :
            return False