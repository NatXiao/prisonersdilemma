class Player:
    points = []
    opponentsMove = []

    def getPoint(self, res: int):
        self.points.append(res)

    def decide(self):
        raise NotImplemented()

    def printPoint(self):
        print(sum(self.points))

    def updateOpponentsMove(self, ans: bool):
        self.opponentsMove.append(ans)
