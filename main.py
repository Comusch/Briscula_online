import Card as cd
import Game
'''
d = cd.Deck()
d.output_deck()
print("------shuffle begin----")
d.shuffle()
print("------new Deck-----")
d.output_deck()'''

g = Game.Game(5)
print("------players ----")
g.output_players(0)
g.output_players(1)
g.output_players(2)
g.output_players(3)
g.output_players(4)
print("--------start Game--------")
g.set_trumpf(1)
for i in range(0, 8):
    g.players[0] = g.play_Card(0, g.players[0])
    g.players[1] = g.play_Card(0, g.players[1])
    g.players[2] = g.play_Card(0, g.players[2])
    g.players[3] = g.play_Card(0, g.players[3])
    g.players[4] = g.play_Card(0, g.players[4])
    print("--------stack set----------")
    g.output_Stack()
    print(f"winner of the stack: {g.check_win_Stack()[1]} ")
    g.clear_stack()


