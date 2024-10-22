# Write a function that takes an array of words and smashes them together 
# into a sentence and returns the sentence. You can ignore any need to 
# sanitize words or add punctuation, but you should add spaces between 
# each word. Be careful, there shouldn't be a space at the beginning or 
# the end of the sentence!

# Example
# ['hello', 'world', 'this', 'is', 'great']  =>  'hello world this is great'

# -------------------------------------------------------------------------------------
# -----Solution 1-----Join Method-----
def smash(words):
    return " ".join(words)
#   1.  We define a () called smash that takes a list of words as input.
#   2.  Then use the join() similar to Javascript's join() method to concatenate the words in the list.
#   3.  We use a space " " as the separator to add spaces between the words.
#   4.  Finally, we return the concatenated sentence.

# -------------------------------------------------------------------------------------
# -----Solution 2-----Store Join Method in Variable-----
smash = ' '.join
#   1.  We define a variable smash that is assigned to the join() method.
#   2.  The join() method is used to concatenate the words in the list.
#   3.  We use a space " " as the separator to add spaces between the words.
#   4.  The variable smash is now a reference to the join() method.
#   5.  We can now use smash as a function to concatenate the words in the list.


# -------------------------------------------------------------------------------------
# -----Solution 3-----Join Method w/ Strip-----
def smash(words):
    return ' '.join(words).strip()
#   1.  We define a () called smash that takes a list of words as input.
#   2.  Then use the join() method to concatenate the words in the list.
#   3.  We use a space " " as the separator to add spaces between the words.
#   4.  We use the strip() method to remove any leading or trailing whitespace 
#       from the concatenated sentence.
#   5.  Finally, we return the concatenated sentence.

# -------------------------------------------------------------------------------------
# -----Solution 4-----Javascript Solution-----
# smash = function (words) {
#   return words.join(" ");
# };
#   1.  We define a function smash that takes a list of words as input.
#   2.  Then use the join() method to concatenate the words in the list.
#   3.  We use a space " " as the separator to add spaces between the words.
#   4.  The result is returned.

#   This is similar to Python Solution 1 but is written in Javascript. 
#   The join() method is used to concatenate