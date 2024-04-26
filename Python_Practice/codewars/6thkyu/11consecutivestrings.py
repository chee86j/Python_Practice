# DESCRIPTION:
# You are given an array(list) strarr of strings and an integer k. Your task 
# is to return the first longest string consisting of k consecutive strings 
# taken in the array.

# Examples:
# strarr = ["tree", "foling", "trashy", "blue", "abcdef", "uvwxyz"], k = 2

# Concatenate the consecutive strings of strarr by 2, we get:

# treefoling   (length 10)  concatenation of strarr[0] and strarr[1]
# folingtrashy ("      12)  concatenation of strarr[1] and strarr[2]
# trashyblue   ("      10)  concatenation of strarr[2] and strarr[3]
# blueabcdef   ("      10)  concatenation of strarr[3] and strarr[4]
# abcdefuvwxyz ("      12)  concatenation of strarr[4] and strarr[5]

# Two strings are the longest: "folingtrashy" and "abcdefuvwxyz".
# The first that came is "folingtrashy" so 
# longest_consec(strarr, 2) should return "folingtrashy".

# In the same way:
# longest_consec(["zone", "abigail", "theta", "form", "libe", "zas", "theta", 
#                 "abigail"], 2) --> "abigailtheta"
# n being the length of the string array, if n = 0 or k > n or k <= 0 return "" 
# (return Nothing in Elm, "nothing" in Erlang).

# Note
# consecutive strings : follow one after another without an interruption

# -------------------------------------------------------------------------------------
# -----Solution 1-----
def longest_consec(strarr, k):
    result = ""
    
    if k > 0 and len(strarr) >= k:
        for index in range(len(strarr) - k + 1):
            s = ''.join(strarr[index:index+k])
            if len(s) > len(result):
                result = s
            
    return result
#   1.  Create a () that takes in two arguments, strarr and k
#   2.  Create a var result and set it to an empty string
#   3.  Check if k is greater than 0 and length of strarr is greater than or equal to k
#   4.  Create a for loop that will iterate through range of length of strarr - k + 1
#   5.  Create a var s and set it to concatenation of k consecutive strings in strarr
#   6.  Check if length of s is greater than length of result
#   7.  Set result to s
#   8.  Return result

# -------------------------------------------------------------------------------------
# -----Solution 2-----
def longest_consec(strarr, k):
    if k <= 0 or k > len(strarr):
        return ''

    starr_lengths = list(map(len, strarr))
    temp_max_len = 0
    position = 0

    for p in range(len(starr_lengths) - (k - 1)):
        set_sum = 0
        for i in range(k):
            set_sum += starr_lengths[p+i]
        
        if set_sum > temp_max_len:
            temp_max_len = set_sum
            position = p

    return ''.join([s for s in strarr[position:position+k]])
#   1.  Create a () that takes in two arguments, strarr and k
#   2.  Check if k is less than or equal to 0 or k is greater than length of strarr
#   3.  Return an empty string
#   4.  Create a list starr_lengths that will store length of each string in strarr
#   5.  Create a var temp_max_len and set it to 0
#   6.  Create a var position and set it to 0
#   7.  Create a for loop that will iterate through range of length of starr_lengths - (k - 1)
#   8.  Create a var set_sum and set it to 0
#   9.  Create a nested for loop that will iterate through range of k
#   10. Add length of string at index p + i to set_sum
#   11. Check if set_sum is greater than temp_max_len
#   12. Set temp_max_len to set_sum
#   13. Set position to p
#   14. Return concatenation of k consecutive strings in strarr starting from position
