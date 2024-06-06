# Instructions
# Write a function that takes a single non-empty string of 
# only lowercase and uppercase ascii letters (word) as its 
# argument, and returns an ordered list containing the 
# indices of all capital (uppercase) letters in the string.

# Example (Input --> Output)
# "CodEWaRs" --> [0,3,4,6]

# -------------------------------------------------------------------------------------
# -----Solution 1-----List Comprehension with Enumerate & Isupper-----
def capitals(word):
    return [i for (i, c) in enumerate(word) if c.isupper()]
#  Enumerate returns idx and value of each element in list
#  Isupper checks if char is uppercase by returning True or False
#  1.  Return idx of char if char is uppercase
#      with isupper() method built into Python where True is uppercase and False is lowercase
#  2.  Iterate through each char in word using enumerate
#      which returns idx and char of each element in list
#  3.  Check if char is uppercase
#  4.  Return idx of char if it is uppercase

# -------------------------------------------------------------------------------------
# -----Solution 2-----If Statement & Append & Isupper-----
def capitals(word):
    uppers = []
    for i in range(len(word)):
        if word[i].isupper():
            uppers.append(i)
    return uppers
#  1.  Create an empty list to store indices of uppercase chars
#  2.  Iterate through each idx in range of length of word
#  3.  Check if char at idx is uppercase
#  4.  Append idx to list if char is uppercase
#  5.  Return list of uppercase indices

# -------------------------------------------------------------------------------------
# -----Solution 3-----Javascript Solution-----
# var capitals = function (word) {
#   var caps = [];
# 	for(var i = 0; i < word.length; i++) {
#     if(word[i].toUpperCase() == word[i]) caps.push(i);
#   }
#   return caps;
# };

#  1. Create an empty list to store indices of uppercase chars
#  2. Iterate through each idx in range of length of word
#  3. Check if char at idx is uppercase by comparing char 
#     to uppercase version of char
#  4. Append idx to list if char is uppercase
#  5. Return list of uppercase indices
