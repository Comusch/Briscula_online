import Card as cd
import Game
'''
d = cd.Deck()
d.output_deck()
print("------shuffle begin----")
d.shuffle()
print("------new Deck-----")
d.output_deck()


#input aus konsole
answer = input("Wie heißt du?")
print(f"Dein Name ist {answer}")


g = Game.Game(5)
print("------players ----")
g.output_players(0)
g.output_players(1)
g.output_players(2)
g.output_players(3)
g.output_players(4)
print("--------start Game--------")
g.Gamestart()
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
    g.clear_stack()'''
#test if the game works
print("--------Test if the game works--------")
player_ids= [1, 2, 3, 4, 5]
g = Game.Game(5, player_ids)
g.Gamestart(0)
print("------players ----")
g.output_players(0)
g.output_players(1)
g.output_players(2)
g.output_players(3)
g.output_players(4)
print("--------start Game--------")
print("--------player bets, who will play--------")
g.players[0] = g.add_Bet(g.players[0], 20)
# Loop through each player's bet
for j in range(0, 7):
    # Check if it's player 2's turn to bet
    i = g.current_player_nr
    if j == 0:
        # Player 2 bets
        g.players[i] = g.add_Bet(g.players[i], 1)
    else:
        # Other players bet 20
        g.players[i] = g.add_Bet(g.players[i], 20)

# After all players have bet, check if player 2 should play
if g.agree_number == 4:
    print(f"The player with the id: {g.select_player.id} will play.")
else:
    print("Not all players agreed, game cannot proceed.")

print(f"the player with the id: {g.select_player.id} will play")
print("--------player select trumpf--------")
g.select_player = g.Select_Trumpf(g.select_player, 1)
print("Caller Team:")
for p in g.caller_group:
    print(p.id)
print("Defender Team:")
for p in g.defender_group:
    print(p.id)
print(f"the trumpf is: {g.trumpf}")
print("--------player play cards--------")
for i in range(0, 8):
    for j in range(0,5):
        k = g.current_player_nr
        g.players[k] = g.play_Card(0, g.players[k])
    print("--------stack set----------")
    g.output_Stack()
    print(f"winner of the stack: {g.check_win_Stack()[1]} ")
    g.end_of_round()

print("--------end of the playing--------")

winner = g.End_of_Game()

print(f"the winner of the game are:")
for p in winner:
    print(p.id)

print("--------end of the test------------")
print("now you can start a new game")






