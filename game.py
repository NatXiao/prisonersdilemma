import random
from Player import Player
from players.TitForTat import TitForTat
from players.randomPlayer import RandomPlayer
from players.NonForgiver import NonForgiver
from players.TitForTwoTat import TitForTwoTat


class PrisonersDilemma:
    player0: Player
    player1: Player
    nb_round: int
    probabilistic : int
    gameState: list
    

    def __init__(self, player0: Player, player1: Player, nb_round: int = 200, probabilistic: int = 10):
        assert(probabilistic >0 and 100> probabilistic)
        self.player0 = player0
        self.player1 = player1
        self.nb_round = nb_round
        self.probabilistic = probabilistic
        self.gameState = [0, 0, 0, 0]

    def simulateRound(self):
        ans0 = self.player0.decide()
        ans1 = self.player1.decide()
        if ans0 and ans1:
            self.player0.getPoint(3)
            self.player1.getPoint(3)
            self.gameState[0] += 1
        elif ans0:
            self.player1.getPoint(5)
            self.player0.getPoint(0)
            self.gameState[1] += 1
        elif ans1:
            self.player0.getPoint(5)
            self.player1.getPoint(0)
            self.gameState[2] += 1
        else:
            self.player0.getPoint(1)
            self.player1.getPoint(1)
            self.gameState[3] += 1
        ans0 = self.addError(ans0)
        ans1 = self.addError(ans1)
        self.player0.updateOpponentsMove(ans1)
        self.player1.updateOpponentsMove(ans0)

    def addError(self, res: bool):
        if (random.random() * 100) > self.probabilistic:
            return res
        else:
            return not res

    def launch(self):
        self.player0.points = []
        self.player1.points = []
        for i in range(self.nb_round):
            self.simulateRound()
        print(self.gameState)

#game = PrisonersDilemma(player0=algo0, player1=algo1)
#game.launch()
