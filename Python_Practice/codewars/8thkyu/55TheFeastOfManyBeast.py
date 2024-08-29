# All of the animals are having a feast! Each animal is bringing one dish. 
# There is just one rule: the dish must start and end with the same letters 
# as the animal's name. For example, the great blue heron is bringing 
# garlic naan and the chickadee is bringing chocolate cake.

# Write a function feast that takes the animal's name and dish as arguments 
# and returns true or false to indicate whether the beast is allowed to 
# bring the dish to the feast.

# Assume that beast and dish are always lowercase strings, and that each has 
# at least two letters. beast and dish may contain hyphens and spaces, but 
# these will not appear at the beginning or end of the string. They will 
# not contain numerals.

# -------------------------------------------------------------------------------------
# -----Solution 1----Indexing-----
def feast(beast, dish):
    return beast[0] == dish[0] and beast[-1] == dish[-1]
#   1.  The ()) takes two strings, `beast` & `dish`, as input.
#   2.  It returns True if the first character of `beast` is equal to the first character of `dish`
#       and the last character of `beast` is equal to the last character of `dish`. Otherwise, it returns False.
#   3.  This solution has a time complexity of O(1) because it performs a constant number of comparisons
#       regardless of the length of the input strings. The space complexity is also O(1) because the ()
#       uses a constant amount of extra space.


# -------------------------------------------------------------------------------------
# -----Solution 2----Startswith & Endswith-----
def feast(beast, dish):
    return beast.startswith(dish[0]) and beast.endswith(dish[-1])
#   1.  This solution uses the startswith() & endswith() methods to check if the first character of `beast`
#       is equal to the first character of `dish` and the last character of `beast` is equal to the last character of `dish`.
#   2.  If both conditions are met, the () returns True. Otherwise, it returns False.
#   3.  This solution has a time complexity of O(1) because the startswith() & endswith() methods perform a constant
#       number of comparisons regardless of the length of the input strings. The space complexity is also O(1) because
#       the () uses a constant amount of extra space. Compared to Solution 1, this solution uses built-in methods
#       that provide a more readable and concise way to check the conditions.

# -------------------------------------------------------------------------------------
# -----Solution 3----Javascript Solution-----Indexing-----
# function feast(beast, dish) {
# 	return beast[0] === dish[0] && beast[beast.length - 1] === dish[dish.length - 1]
# }
#   1.  This Javascript solution is similar to Solution 1. It uses indexing to check if the first character of `beast`
#       is equal to the first character of `dish` and the last character of `beast` is equal to the last character of `dish`.
#   2.  If both conditions are met, the () returns true. Otherwise, it returns false.
#   3.  This solution has a time complexity of O(1) because it performs a constant number of comparisons regardless of
#       the length of the input strings. The space complexity is also O(1) because the () uses a constant amount of
#       extra space. This solution is concise and straightforward, using simple comparisons to check the conditions.