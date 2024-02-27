import Card as cd
import Player as ply

class Game:

    def __init__(self, numb_player):
        #create deck
        self.deck = cd.Deck()
        self.deck.shuffle()
        #create (numb_player) player
        #self.numb_player = numb_player
        self.numb_player = 5
        self.players = []
        for i in range(0, self.numb_player):
            self.players.append(ply.Player(i))
        #give the players diffrend hands
        if self.numb_player == 5:
            for i in range(0, 8):
                for i in range(0, self.numb_player):
                    self.players[i].get_Card(self.deck.cards[0])
                    self.deck.cards.remove(self.deck.cards[0])
            print("hi")

    def round_get_one_card(self):
        for i in range (0, self.numb_player):
            self.players[i].get_Card(self.deck.cards[len(self.deck.cards)-i])
            self.deck.cards.remove(self.deck.cards[len(self.deck.cards)-i])

    def output_players(self, nr):
        print(f"Player id: {self.players[nr].id}")
        print("Player Hand: ")
        for i in range(0,len(self.players[nr].hand)):
            print(f"Card {self.players[nr].hand[i].id}, {self.players[nr].hand[i].color}, {self.players[nr].hand[i].value}")
        print("----------------------")
