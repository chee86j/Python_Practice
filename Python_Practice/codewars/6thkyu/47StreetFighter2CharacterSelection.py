##### Short Intro #####

# Some of you might remember spending afternoons playing Street Fighter 2 in some 
# Arcade back in the 90s or emulating it nowadays with the numerous emulators for 
# retro consoles.

# Can you solve this kata? Suuure-You-Can!

# UPDATE: a new kata's harder version is available here at 
# https://www.codewars.com/kata/street-fighter-2-character-selection-part-2/python.



##### The KATA #####

# You'll have to simulate the video game's character selection screen behaviour, 
# more specifically the selection grid. Such screen looks like this:

# Screen:

# https://images.duckduckgo.com/iu/?u=http%3A%2F%2Fwww.fightersgeneration.com%2Fnp5%2Fgm%2Fsf2ce-s2.jpg&f=1

# ---------------SELECTION GRID LAYOUT IN TEXT---------------#

# | Ryu  | E.Honda | Blanka  | Guile   | Balrog | Vega    |
# | Ken  | Chun Li | Zangief | Dhalsim | Sagat  | M.Bison |

# ---------------INPUT---------------#

# the list of game characters in a 2x6 grid;
# the initial position of the selection cursor (top-left is (0,0));
# a list of moves of the selection cursor (which are up, down, left, right);

# ---------------OUTPUT---------------#

# the list of characters who have been hovered by the selection cursor after all 
# the moves (ordered and with repetition, all the ones after a move, whether 
# successful or not, see tests);


# ---------------RULES---------------#

# Selection cursor is circular horizontally but not vertically!

# As you might remember from the game, the selection cursor rotates horizontally 
# but not vertically; that means that if I'm in the leftmost and I try to go left 
# again I'll get to the rightmost (examples: from Ryu to Vega, from Ken to M.Bison) 
# and vice versa from rightmost to leftmost.

# Instead, if I try to go further up from the upmost or further down from the 
# downmost, I'll just stay where I am located (examples: you can't go lower than 
# lowest row: Ken, Chun Li, Zangief, Dhalsim, Sagat and M.Bison in the above image;
# you can't go upper than highest row: Ryu, E.Honda, Blanka, Guile, Balrog and Vega 
# in the above image).

# ---------------TEST---------------#

# For this easy version the fighters grid layout and the initial position will 
# always be the same in all tests, only the list of moves change.

# Notice: changing some of the input data might not help you.

# ---------------EXAMPLES---------------#

# fighters = [
#   ["Ryu", "E.Honda", "Blanka", "Guile", "Balrog", "Vega"],
#   ["Ken", "Chun Li", "Zangief", "Dhalsim", "Sagat", "M.Bison"]
# ]
# initial_position = (0,0)
# moves = ['up', 'left', 'right', 'left', 'left']

# then I should get:

# ['Ryu', 'Vega', 'Ryu', 'Vega', 'Balrog']
# as the characters I've been hovering with the selection cursor during my moves. 
# Notice: Ryu is the first just because it "fails" the first up See test cases for 
# more examples.

# fighters = [
#   ["Ryu", "E.Honda", "Blanka", "Guile", "Balrog", "Vega"],
#   ["Ken", "Chun Li", "Zangief", "Dhalsim", "Sagat", "M.Bison"]
# ]
# initial_position = (0,0)
# moves = ['right', 'down', 'left', 'left', 'left', 'left', 'right']

# ---------------RESULT---------------#

# ['E.Honda', 'Chun Li', 'Ken', 'M.Bison', 

# -------------------------------------------------------------------------------------
# -----Solution 1-----Grid Using List Comprehension-----
MOVES = {"up": (-1, 0), "down": (1, 0), "right": (0, 1), "left": (0, -1)}

def street_fighter_selection(fighters, initial_position, moves):
    y, x = initial_position
    hovered_fighters = []
    for move in moves:
        dy, dx = MOVES[move]
        y += dy
        if not 0 <= y < len(fighters):
            y -= dy
        x = (x + dx) % len(fighters[y])
        hovered_fighters.append(fighters[y][x])
    return hovered_fighters
#   1.  We start by defining a dictionary called MOVES that maps each move to its 
#       corresponding change in position. 
#   2.  We initialize the y and x coordinates of the current position using the
#       initial_position tuple. `y, x = initial_position`
#   3.  We initialize an empty list called hovered_fighters to store the fighters
#       that the selection cursor will hover over.
#   4.  We iterate over each move in the moves list.
#       For each move, we retrieve the corresponding change in position from the
#       MOVES dictionary using the move as the key. `dy, dx = MOVES[move]`
#   5.  We update the y coordinate by adding dy to the current y value.
#       If the new y value is outside the range of valid indices for the fighters
#       (i.e., not between 0 and len(fighters)), we subtract dy from y to keep it
#       w/in the valid range. `if not 0 <= y < len(fighters): y -= dy`
#   6.  We update the x coordinate by adding dx to the current x value and taking
#       the modulus w/ the number of columns in the current row to ensure it wraps
#       around horizontally. `x = (x + dx) % len(fighters[y])`
#   7.  We append the fighter at the new position to the hovered_fighters list.
#   8.  Finally, we return the list of hovered fighters.

#   This has a time complexity of O(n) where n is the number of moves, and a space
#   complexity of O(1) since we are using a fixed amount of extra space. It is best
#   suited for scenarios where the number of moves is relatively small compared to
#   the size of the fighters grid.

# -------------------------------------------------------------------------------------
# -----Solution 2-----Using If Else-----
def street_fighter_selection(fighters, initial_position, moves):
    cur_pos = [initial_position[0], initial_position[1]]
    selected_fighters = []

    for move in moves:
        if move == "up": 
            cur_pos[0] = 0
        elif move == "down": 
            cur_pos[0] = 1
        elif move == "right":
            cur_pos[1] = (cur_pos[1] + 1) % 6
        elif move == "left":
            cur_pos[1] = (cur_pos[1] - 1) % 6
        selected_fighters.append(fighters[cur_pos[0]][cur_pos[1]])

    return selected_fighters
#   1.  We start by defining a function called street_fighter_selection that takes
#       three parameters: fighters (a 2D list representing the fighters grid),
#       initial_position (a tuple representing the starting position of the cursor),
#       and moves (a list of moves to be performed).
#   2.  We initialize a list called cur_pos w/ the initial position of the cursor.
#   3.  We initialize an empty list called selected_fighters to store the fighters
#       that the cursor will select.
#   4.  We iterate over each move in the moves list.
#       For each move, we check if the move is "up" or "down" and update the row
#       accordingly. If the move is "right" or "left", we update the column
#       accordingly, wrapping around if necessary using the modulus operator.
#   5.  We append the fighter at the current position to the selected_fighters list.
#   6.  Finally, we return the list of selected fighters.

#   This has a time complexity of O(n) where n is the number of moves, and a space
#   complexity of O(1) since we are using a fixed amount of extra space. It is best
#   suited for scenarios datasets w/ relatively few rows. Simpler grids with fixed
#   dimentions are also best suited for this solution.

# -------------------------------------------------------------------------------------
# -----Solution 3-----List Comprehension & Dictionary-----
def street_fighter_selection(fighters, pos, moves):
    r, row, col, m = [], pos[0], pos[1], {"up":(-1, 0), "down":(1, 0), "right":(0, 1), "left":(0,-1)}
    for move in moves:
        row, col = min(max(row + m[move][0], 0), 1), (col + m[move][1]) % 6
        r.append(fighters[row][col])
    return r
#   1.  We start by defining a function called street_fighter_selection that takes
#       three parameters: fighters (a 2D list representing the fighters grid),
#       initial_position (a tuple representing the starting position of the cursor),
#       and moves (a list of moves to be performed).
#   2.  We initialize a list called r to store the selected fighters.
#   3.  We extract the row and column indices from the initial position tuple.
#   4.  We create a dictionary called m that maps each move to its corresponding
#       change in position.
#   5.  We iterate over each move in the moves list.
#       For each move, we update the row and column indices using the corresponding
#       change in position from the m dictionary. We use the min and max functions
#       to ensure that the row index stays w/in the bounds of 0 and 1.
#       We use the modulus operator to ensure that the column index wraps around
#       horizontally.
#   6.  We append the fighter at the new position to the r list.
#   7.  Finally, we return the list of selected fighters.

#   This has a time complexity of O(n) where n is the number of moves, and a space
#   complexity of O(1) since we are using a fixed amount of extra space. It is best
#   suited for scenarios where the number of moves is relatively small compared to
#   the size of the fighters grid. This is best for small grids w/ fixed dimentions.

# -------------------------------------------------------------------------------------
# -----Solution 4-----JavaScript Solution-----
# function streetFighterSelection(fighters, position, moves){
#   var result = [];
  
#   moves.forEach(function(move) {
#     if (move === "up") {
#       position[0] = 0;
#     }
#     else if (move === "down") {
#       position[0] = 1;
#     }
#     else if (move === "right") {
#       position[1] = (position[1] === 5) ? 0 : position[1] + 1;
#     }
#     else if (move === "left") {
#       position[1] = (position[1] === 0) ? 5 : position[1] - 1;
#     }
    
#     result.push(fighters[position[0]][position[1]]);
#   });
  
#   return result;
# }
#   1.  We start by initialising an empty result array.
#   2.  We iterate over each move in the moves array.
#       For each move, we check if the move is "up" or "down" and update the row
#       accordingly. If the move is "right" or "left", we update the column
#       accordingly, wrapping around if necessary using the modulus operator.
#   3.  We append the fighter at the current position to the result array.
#   4.  Finally, we return the result array.

#   This has a time complexity of O(n) where n is the number of moves, and a space
#   complexity of O(1) since we are using a fixed amount of extra space. It is the 
#   best straightforward solution for this problem.
