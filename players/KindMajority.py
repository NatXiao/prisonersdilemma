from Player import Player

class KindMajority(Player):
    def decide(self):
        if self.opponentsMove:
            print(sum(self.opponentsMove), len(self.opponentsMove)/2)
            if sum(self.opponentsMove)>= len(self.opponentsMove)/2:
                return True
            else :
                return False
        return True