# There is a war and nobody knows - the alphabet war!
# There are two groups of hostile letters. The tension between left side letters and 
# right side letters was too high and the war began.

# ===Task===
# Write a function that accepts fight string consists of only small letters and return 
# who wins the fight. When the left side wins return Left side wins!, when the right 
# side wins return Right side wins!, in other case return Let's fight again!.

# The left side letters and their power:

#  w - 4
#  p - 3
#  b - 2
#  s - 1
 
# The right side letters and their power:

#  m - 4
#  q - 3
#  d - 2
#  z - 1
 
# The other letters don't have power and are only victims.

# Example
# AlphabetWar("z");        //=> Right side wins!
# AlphabetWar("zdqmwpbs"); //=> Let's fight again!
# AlphabetWar("zzzzs");    //=> Right side wins!
# AlphabetWar("wwwwwwz");  //=> Left side wins!

# -------------------------------------------------------------------------------------
# -----Solution 1-----Dictionary w/ Ternary Operator & Sum-----
def alphabet_war(fight):
    d = {'w':4,'p':3,'b':2,'s':1,
         'm':-4,'q':-3,'d':-2,'z':-1}
    r = sum(d[c] for c in fight if c in d)
    
    return {r==0:"Let's fight again!",
            r>0:"Left side wins!",
            r<0:"Right side wins!"
            }[True]
#   1. A dictionary 'd' maps each letter to its respective power values.
#      'w':4,'p':3,'b':2,'s':1,'m':-4,'q':-3,'d':-2,'z':-1
#   2. 'sum(d[c] for c in fight if c in d)' calculates the total power score by summing
#      the power values of each letter in the input fight string.
#   3. A dictionary is used to map the results 'r == 0', 'r > 0', and 'r < 0' to their
#      respective output strings.
#   4. Finally the ternary operator is used to return the correct output string based on the
#      result of the fight.

#   The time complexity of this solution is O(n), where n is the length of the input string
#   'fight'. It iterates over each character in the input string once only.
#   The space complexity is O(1) because the dictionary 'd', a constant size, and no additional
#   data structures are used that grow with the input size.

#   This solution is simple and consise, but may be harder to understand for beginners due to
#   the use of dictionary and ternary operator. It is efficient and works well for the given
#   problem, providing a clear and concise solution to the problem.

#   Note that in JS terms, a dictionary is called an object, and the ternary operator is the 
#   same as in Python. 

# -------------------------------------------------------------------------------------
# -----Solution 2-----Find Method & Ternary Operator-----
def alphabet_war(fight):
    result = sum("zdqm".find(c) - "sbpw".find(c) for c in fight)
    return "{} side wins!".format("Left" if result < 0 else "Right") if result else "Let's fight again!"
#   1. The expression 'sum("zdqm".find(c) returns the index of the character 'c' in the right
#      side string; 'sbpw'.find(c) does the same for the left side string. The difference of
#      these two values is calculated for each character in the input string.
#   2. The total score is summed for all characters in fight.
#   3. The ternary operator is used to return the correct output string based on the result of
#      the fight. If the result is 0, it returns "Let's fight again!". Otherwise, it returns
#      "Left side wins!" if the result is negative, and "Right side wins!" if the result is positive.

#   The time complexity of this solution is O(n), where 'n' is the length of 'fight' and 'm' is the
#   length of the strings "zdqm" and "sbpw". The find method has a time complexity of O(m), and it
#   is called for each character in the input string. 
#   The space complexity is O(1) because no additional data structures are used that grow with the

#   This solution is concise and efficient without using a dictionary. It is less efficient than
#   the previous solution because the find method has a time complexity of O(m) and is not as good
#   for beginners due to the use of the find method and the ternary operator. 


# -------------------------------------------------------------------------------------
# -----Solution 3-----Two Dictionaries & Sum-----
def alphabet_war(fight):
  left = {'w':4,'p':3,'b':2,'s':1}
  rigth = {'m':4,'q':3,'d':2,'z':1}
  leftp = 0
  rigthp = 0
  for e in fight:
    leftp += left.get(e,0)
    rigthp += rigth.get(e,0)
  if leftp > rigthp:
    return'Left side wins!'
  elif rigthp > leftp:
    return 'Right side wins!'
  else:
    return "Let's fight again!"
#   1. Two dictionaries 'left' and 'right' are created to map the power values of the letters
#      on the left and right sides respectively.
#   2. Two variables 'leftp' and 'rightp' are initialized to 0 to store the total power of the
#      left and right sides respectively.
#   3. A for loop iterates over each character in the input string 'fight'.
#   4. The power value of the current character is added to the corresponding side's total power.
#   5. The get method is used to retrieve the power value of the current character from the
#      dictionary. If the character is not in the dictionary, it returns 0.
#   6. After calculating the total power of both sides, the function compares the two values to
#      determine the winner.
#   7. If the total power of the left side is greater than that of the right side, it returns
#      'Left side wins!'. If the total power of the right side is greater, it returns 'Right side
#      wins!'. Otherwise, it returns "Let's fight again!".

#   The time complexity of this solution is O(n), where n is the length of the input string 'fight'.
#   The for loop iterates over each character in the input string once.
#   The space complexity is O(1) because the dictionaries 'left' and 'right' are of constant size,
#   and no additional data structures are used that grow with the input size.

#   This solution is simple and easy to understand, as it uses two dictionaries to store the power
#   values of the letters on the left and right sides. It is efficient and provides a clear solution
#   to the problem without using complex operations or data structures.
#   Compared to the other solutions, this one is more straightforward and beginner-friendly, making
#   it easier to follow and implement. Definitely more verbose.

# -------------------------------------------------------------------------------------
# -----Solution 4-----JavaScript Solution-----
# function alphabetWar(fight) {
#     let map = { w: -4, p: -3, b: -2, s: -1, m: 4, q: 3, d: 2, z: 1 };
#     let result = fight.split('').reduce((a, b) => a + (map[b] || 0), 0);
#     return result ? (result < 0 ? "Left" : "Right") + " side wins!" : "Let's fight again!";
# }
#   This JavaScript solution is similar to the first Python solution. It uses a dictionary to map
#   the power values of the letters on the left and right sides. It then uses the reduce method
#   to calculate the total power of each side by summing the power values of the characters in the
#   input string. Finally, it returns the result based on the total power values, similar to the

#   The reduce method leveraged here might be less intuitive for beginners, but it is a concise way
#   to calculate the sum of the power values. The solution is efficient and provides a clear and
#   concise way to solve the problem in JavaScript.

#   The time complexity of this solution is O(n), where n is the length of the input string 'fight'.
#   The space complexity is O(1) because the dictionary 'map' is of constant size, and no additional
#   data structures are used that grow with the input size.
