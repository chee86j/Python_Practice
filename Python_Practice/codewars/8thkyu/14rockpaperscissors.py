# Rock Paper Scissors

# Let's play! You have to return which player won! In case of a draw return Draw!.

# Examples(Input1, Input2 --> Output):

# "scissors", "paper" --> "Player 1 won!"
# "scissors", "rock" --> "Player 2 won!"
# "paper", "paper" --> "Draw!"

# -------------------------------------------------------------------------------------
# -----Solution 1-----Dictionary-----
def rps(p1, p2):
    beats = {'rock': 'scissors', 'scissors': 'paper', 'paper': 'rock'}
    if beats[p1] == p2:
        return "Player 1 won!"
    if beats[p2] == p1:
        return "Player 2 won!"
    return "Draw!"
    # uses a dictionary 'beats' to determine the winner of the game
    # the dictionary has the following key-value pairs:
    # 'rock' beats 'scissors'
    # 'scissors' beats 'paper'
    # 'paper' beats 'rock'
    # if p1 beats p2, return "Player 1 won!"
    # if p2 beats p1, return "Player 2 won!"

# -------------------------------------------------------------------------------------
# -----Solution 2-----Using 2 Dictionaries-----
def rps(p1, p2):
    hand = {'rock':0, 'paper':1, 'scissors':2}
    results = ['Draw!', 'Player 1 won!', 'Player 2 won!']
    return results[hand[p1] - hand[p2]]
    # uses 2 dictionaries to determine the winner of the game
    # each dictionary has its own key-value pairs
    # finally, it returns the result of the game using the results list

# -------------------------------------------------------------------------------------
# -----Solution 3-----If-Elif-Else-----
def rps(player1, player2):
    if player1 == player2:
        return "Draw!"
    elif (player1 == "rock" and player2 == "scissors") or (player1 == "scissors" and player2 == "paper") or (player1 == "paper" and player2 == "rock"):
        return "Player 1 won!"
    else:
        return "Player 2 won!"
    # this solution uses if-elif-else statements to determine the winner of the game
    # it lists all the possible outcomes of the game and returns the result
