# You get any card as an argument. Your task is to return the suit of this 
# card (in lowercase).

# Our deck (is preloaded):

# DECK = ['2S','3S','4S','5S','6S','7S','8S','9S','10S','JS','QS','KS','AS',
#         '2D','3D','4D','5D','6D','7D','8D','9D','10D','JD','QD','KD','AD',
#         '2H','3H','4H','5H','6H','7H','8H','9H','10H','JH','QH','KH','AH',
#         '2C','3C','4C','5C','6C','7C','8C','9C','10C','JC','QC','KC','AC']

# ('3C') -> return 'clubs'
# ('3D') -> return 'diamonds'
# ('3H') -> return 'hearts'
# ('3S') -> return 'spades'

# -------------------------------------------------------------------------------------
# -----Solution 1-----Dictionary-----
def define_suit(card):
    d = {'C': 'clubs', 'S':'spades', 'D':'diamonds','H':'hearts'}
    return d[card[-1]]
#   1. 'd' is a dictionary that maps the suit symbol to the suit name
#   2. We are returning the value (suit) of the key card[-1] from the dictionary 'd'
#   3. 'd[card[-1]]' will return the value of the key card[-1] from the dictionary 'd'
#   4. card[-1] will return the last character of the string 'card'

#   The time complexity of this solution is O(1) as we are using a dictionary to store
#   the suit values & the space complexity is O(1) as we are storing the suit values in
#   a dictionary

# -------------------------------------------------------------------------------------
# -----Solution 2-----Concise Dictionary-----
def define_suit(card):
    return {'C':'clubs', 'S':'spades', 'D':'diamonds', 'H':'hearts'}[card[-1]]
#   1. Similar to Solution 1, we are returning the value of the key card[-1] from the
#      dictionary {'C':'clubs', 'S':'spades', 'D':'diamonds', 'H':'hearts'}
#   2. The dictionary is created inline in the return statement with 'card[-1]' as the key

#   The time complexity of this solution is O(1) as we are using a dictionary to store
#   the suit values & the space complexity is O(1) as we are storing the suit values in
#   a dictionary
  
# -------------------------------------------------------------------------------------
# -----Solution 3-----Javascript Solution-----     
# function defineSuit(card) {
#     const suits = {
#         '♣': 'clubs',
#         '♠': 'spades',
#         '♦': 'diamonds',
#         '♥': 'hearts'
#     };
#     return suits[card.slice(-1)];
# }

#   1. Similar to Solution 1, we are returning the value of the key card.slice(-1) from the
#      dictionary suits
#   2. The dictionary is created inline in the return statement with 'card.slice(-1)' as the key
#   3. card.slice(-1) will return the last character of the string 'card'

#   The time complexity of this solution is O(1) as we are using a dictionary to store
#   the suit values & the space complexity is O(1) as we are storing the suit values in
#   a dictionary

