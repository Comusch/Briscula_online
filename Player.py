
class Player:

    def __init__(self, id):
        self.id = id
        self.action = False
        self.score = 0
        self.hand = []

    def get_Card(self, c):
        self.hand.append(c)



