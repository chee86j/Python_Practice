# We want to know the index of the vowels in a given word, for example, 
# there are two vowels in the word super (the second and fourth letters).

# So given a string "super", we should return a list of [2, 4].

# Some examples:
# Mmmm  => []
# Super => [2,4]
# Apple => [1,5]
# YoMama -> [1,2,4,6]

# NOTES

#     Vowels in this context refers to: a e i o u y (including upper case)
#     This is indexed from [1..n] (not zero indexed!)

# -------------------------------------------------------------------------------------
# -----Solution 1-----One Liner w/ List Comprehension-----
def vowel_indices(word):
    return [i for i,x in enumerate(word,1) if x.lower() in 'aeiouy']
#   1. The vowel_indices() function takes a word as input.
#   2. It uses a list comprehension to iterate over the characters in the word w/
#      'enumerate()' function, which returns the index and character of each element.
#   3. The 'enumerate()' function is used with a start index of 1 to match the output
#      format of the problem.
#   4. It checks if the lowercase version of the character is a vowel using the 'in' operator.
#   5. If the character is a vowel, it appends the index to the list.
#   6. The final result is a list of vowel indices in the word.

#   This solution has a time complexity of O(n) because it iterates over the characters in the word
#   and checks if each character is a vowel. For the space complexity, it is O(n) because the list of
#   vowel indices grows with the size of the word.



# -------------------------------------------------------------------------------------
# -----Solution 2-----
def vowel_indices(word):
    word = word.lower()
    vowels = ['a', 'e', 'i', 'o', 'u', 'y']
    lst = []
    for index in range(len(word)):
        if word[index] in vowels:
            lst.append(index + 1)
    return lst
#   1. The vowel_indices() function takes a word as input.
#   2. It converts the word to lowercase to handle both uppercase and lowercase vowels 'word.lower()'.
#   3. It initializes a list of vowels 'vowels' to check if a character is a vowel.
#   4. It initializes an empty list 'lst' to store the vowel indices.
#   5. It iterates over the indices of the characters in the word using 'range(len(word))'.
#   6. It checks if the character at the current index is a vowel using 'word[index] in vowels'.
#   7. If the character is a vowel, it appends the index + 1 to the list 'lst'.
#   8. The final result is a list of vowel indices in the word.

#   This solution has a time complexity of O(n) because it iterates over the characters in the word
#   and checks if each character is a vowel. For the space complexity, it is O(n) because the list of
#   vowel indices grows with the size of the word. Slighly more verbose than the first solution, but 
#   easier for beginners to understand.


# -------------------------------------------------------------------------------------
# -----Solution 3-----Javacript Solution-----Regular Expression-----
# function vowelIndices(word) {
#   var arr = [];
#   for(var i = 0; i < word.length; i++) {
#     if(/[aeioyu]/i.test(word[i])) {
#       arr.push(i+1);
#     }
#   }
#   return arr;
# }
# 1. The vowelIndices() function takes a word as input.
# 2. It initializes an empty array 'arr' to store the vowel indices.
# 3. It iterates over the characters in the word using a for loop.
# 4. It checks if the character at the current index is a vowel using a regular expression.
# 5. If the character is a vowel, it appends the index + 1 to the array 'arr'.
# 6. The final result is an array of vowel indices in the word.

# This solution has a time complexity of O(n) because it iterates over the characters in the word
# and checks if each character is a vowel using a regular expression. For the space complexity,
# it is O(n) because the array of vowel indices grows with the size of the word. It is a concise
# and efficient solution similar to the first solution in Python.