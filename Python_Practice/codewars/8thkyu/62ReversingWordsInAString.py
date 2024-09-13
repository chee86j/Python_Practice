# You need to write a function that reverses the words in a given string. 
# Words are always separated by a single space.

# As the input may have trailing spaces, you will also need to ignore 
# unneccesary whitespace.

# Example (Input --> Output)

# "Hello World" --> "World Hello"
# "Hi There." --> "There. Hi"

# Happy coding!

# -------------------------------------------------------------------------------------
# -----Solution 1----Split & Slice Notation----
def reverse(st):
    return ' '.join(st.split()[::-1])
#   The split() method is used to split the input str into an arr of words.
#   The arr is then reversed using the slice notation [::-1]. Finally, the join()
#   method is used to join the arr of words into a single str, separated by a space.

# -------------------------------------------------------------------------------------
# -----Solution 2----Reversed & Strip----
def reverse(st):
    return " ".join(reversed(st.split())).strip()
#   This solution uses the reversed() method to reverse the arr of words returned by 
#   the split() method. The join() method is then used to join the reversed arr of words
#   into a single str, separated by a space. The strip() method is used to remove any
#   leading or trailing whitespace from the final output.
