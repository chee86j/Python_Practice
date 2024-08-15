# Given a string of words, you need to 
# find the highest scoring word.

# Each letter of a word scores points 
# according to its position in the 
# alphabet: a = 1, b = 2, c = 3 etc.

# For example, the score of abad is 
# 8 (1 + 2 + 1 + 4).

# You need to return the highest scoring 
# word as a string.

# If two words score the same, return the 
# word that appears earliest in the original string.

# All letters will be lowercase and all 
# inputs will be valid.

# -------------------------------------------------------------------------------------
# -----Solution 1-----One Liner w/List Comprehension & max()-----
def high(x):
    return max(x.split(), key=lambda k: sum(ord(c) - 96 for c in k))
#   1. Split the str 'x' into a list of words using split().
#   2. Use the max() function to find the highest scoring word.
#   3. The key parameter is used to specify a function that is used to determine the
#      "key" for sorting.
#   4. The lambda function `lambda k: sum(ord(c) - 96 for c in k)` calculates the score of each word. 
#      Here, ord(c) - 96 converts each character c to its position in the alphabet (a=1, b=2, etc.), 
#      similar to how charCodeAt() works in JS but adjusted for the alphabet.
#   5. This has a time complexity of O(n) where n is the length of the str 'x' and a
#      space complexity of O(n) where n is the length of the str 'x'.
#      It is efficent for small strings but not for large strings. In terms of readability,
#      this is concise and easy to understand, but might be less readable for beginners due to its compactness.

# -------------------------------------------------------------------------------------
# -----Solution 2-----Iterative Loop & List & max()-----
def high(x):
    words=x.split(' ')
    list = []
    for i in words:
        scores = [sum([ord(char) - 96 for char in i])]
        list.append(scores)
    return words[list.index(max(list))]
#   1. Split the str 'x' into a list of words using split().
#   2. Create an empty list 'list' to store the scores of each word.
#   3. Iterate through the list of words using a for loop.
#   4. In the loop, sum([ord(char) - 96 for char in i]) computes the score of each word. 
#      This is similar to using reduce() in JavaScript.
#   5. Append the score to the 'list' list w/ append().
#   6. Find the idx of the word w/ the highest score using the index() method.
#   7. Return the word w/ the highest score.
#   8. This has a time complexity of O(n) where n is the length of the str 'x' and a
#      space complexity of O(n) where n is the length of the str 'x'.
#      It is efficent for small strings but not for large strings. This solution is more
#      verbose than Solution 1, but it is easier to understand.


# -------------------------------------------------------------------------------------
# -----Solution 3-----Javascript Solution-----
# function high(s){
#   let as = s.split(' ').map(s=>[...s].reduce((a,b)=>a+b.charCodeAt(0)-96,0));
#   return s.split(' ')[as.indexOf(Math.max(...as))];
# }
#   1. This is the same as Solution 2 but in JS. `s.split(' ').map(...)`` splits the str 
#      into words and calculates the score for each word using reduce() in JavaScript. 
#   2. `Math.max(...as)` finds the highest score & `as.indexOf(...)` finds the idx of 
#      the highest score. The word w/ the highest score is returned.

# or

# function high(x){
#   let alphabets = [
#     'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
#     'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
#   ];
  
#   let words = x.split(" ");
#   let highestScore = 0;
#   let highestScoreWord = "";
  
#   for (let word of words) {
#     let lettersSum = 0;
    
#     for (let letter of word) {
#       lettersSum += alphabets.indexOf(letter) + 1;
#     }
    
#     if (lettersSum > highestScore) {
#       highestScore = lettersSum;
#       highestScoreWord = word;
#     }
#   }
  
#   return highestScoreWord;
# }

#   1. This is a more verbose solution that uses a nested loop to calculate the score of each word.
#   2. The outer loop iterates over each word in the input string.
#   3. The inner loop calculates the score of each letter in the word by finding its idx in the alphabet arr
#      and adding 1 to it.
#   4. The word w/ the highest score is stored in the `highestScoreWord` variable.
#      This solution has a time complexity of O(n*m) where n is the number of words in the input string and m is the
#      average length of the words. The space complexity is O(1) as no additional data structures are used.
#      This solution is explicit and easy to understand, making it suitable for beginners.


# -------------------------------------------------------------------------------------
# Final Thoughts

# This problem is excellent for practicing several key programming concepts:
# - String Manipulation: splitting a string into words and iterating over characters.
# - Scoring & Value Calculation: calculating the score of a word based on the position of its letters in the alphabet.
# - List & Data Structure Handling: storing scores in a list and finding the highest score.
# - Algorithm Designing: finding the highest scoring word and handling edge cases.
# - Edge Cases & Input Validation: considering scenarios where multiple words have the same score.
# - Code Optimization: writing concise and efficient code using built-in functions and methods.
# - Code Readability: balancing between concise and readable code to ensure maintainability.