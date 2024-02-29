import Card as cd
import Player as ply

class Game:

    def __init__(self, numb_player):
        #create deck
        self.deck = cd.Deck()
        self.deck.shuffle()
        #trumph default
        self.trumpf = 99
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
        self.stack = []
        self.current_player_nr = 0

    def Gamestart(self):
        #TODO: shuffle the deck and give the players new cards
        self.players[self.current_player_nr].action = True

    #Method play Card
    def play_Card(self, hand_nr, player):
        if player.action:
            self.stack.append((player.hand[hand_nr], player.id))
            player.remove_Card(player.hand[hand_nr])

            if self.current_player_nr +1 >= 5:
                self.current_player_nr = 0
            else:
                self.current_player_nr +=1
            self.players[self.current_player_nr].action = True
            player.action = False
        return player


    #Method set trumpf
    def set_trumpf(self, new_trumpf):
        self.trumpf = new_trumpf

    #Methode check stack gewinn
    def check_win_Stack(self):
        anfangsfarbe = self.stack[0][0].color
        current_highscard = self.stack[0][0]
        current_playerid = self.stack[0][1]
        for step in self.stack:
            if step[0].color == anfangsfarbe:
                if step[0].value > current_highscard.value:
                    current_highscard = step[0]
                    current_playerid = step[1]
                    anfangsfarbe = step[0].color
            elif step[0].color == self.trumpf:
                current_highscard = step[0]
                current_playerid = step[1]
                anfangsfarbe = step[0].color

        return (current_highscard, current_playerid)

    #Methode End of the round
    def end_of_round(self):
        current_highscard, current_playerid = self.check_win_Stack()
        winner = None
        for i in range(0, len(self.players)):
            if self.players[i].id == current_playerid:
                winner = self.players[i]
                self.current_player_nr = i
        winner.collection.append(self.stack)
        self.clear_stack()
        self.players[self.current_player_nr].action = True

    def getScore(self, player):
        for card in player.collection:
            if card.value == 9:
                player.score +=11
            elif card.value == 8:
                player.score +=10
            elif card.value == 7:
                player.score += 4
            elif card.value == 6:
                player.score +=3
            elif card.value == 5:
                player.score +=2
        return player

    def clear_stack(self):
        self.stack = []

    def round_get_one_card(self):
        for i in range (0, self.numb_player):
            self.players[i].get_Card(self.deck.cards[len(self.deck.cards)-i])
            self.deck.cards.remove(self.deck.cards[len(self.deck.cards)-i])

    def output_Stack(self):
        print("-----current stack---------")
        for step in self.stack:
            print(f"Card: color:{step[0].color}, value:{step[0].value}; Player_id: {step[1]}")

    def output_players(self, nr):
        print(f"Player id: {self.players[nr].id}")
        print("Player Hand: ")
        for i in range(0,len(self.players[nr].hand)):
            print(f"Card {self.players[nr].hand[i].id}, {self.players[nr].hand[i].color}, {self.players[nr].hand[i].value}")
        print("----------------------")

