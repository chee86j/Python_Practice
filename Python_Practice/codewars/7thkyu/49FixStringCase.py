# In this Kata, you will be given a string that may have mixed 
# uppercase and lowercase letters and your task is to convert 
# that string to either lowercase only or uppercase only based on:

#    - make as few changes as possible.
#    - if the string contains equal number of uppercase and 
#      lowercase letters, convert the string to lowercase.

# For example:

# solve("coDe") = "code". Lowercase characters > uppercase. Change only the "D" to lowercase.
# solve("CODe") = "CODE". Uppercase characters > lowecase. Change only the "e" to uppercase.
# solve("coDE") = "code". Upper == lowercase. Change all to lowercase.

# -------------------------------------------------------------------------------------
# -----Solution 1-----Counting w/ For Loop-----
def solve(s):
    upper = 0
    lower = 0
    
    for char in s:
        if char.islower():
            lower += 1
        else:
            upper += 1
            
    if upper == lower or lower > upper:
        return s.lower()
    else:
        return s.upper()
#   1.  We start by initializing two counter vars, upper and lower, to 0.
#   2.  Then iterate through each char in the str.
#       a.  If the char is lowercase, increment the lower counter.
#       b.  If the char is uppercase, increment the upper counter.
#   3.  We then check if the number of uppercase chars is equal to the number of lowercase chars
#       or if the number of lowercase chars is greater than the number of uppercase chars.
#       a.  If either of these conditions is true, we return the str in lowercase.
#       b.  Otherwise, we return the str in uppercase.

#   The time complexity of this solution is O(n) as it goes through each char in the str once.
#   The space complexity is O(1) as we only use a fixed amount of space to store the counters
#   regardless of the size of the input str.
    
# -------------------------------------------------------------------------------------
# -----Solution 2-----Functional One-Liner Approach-----
def solve(s):
    return s.upper() if sum(map(str.isupper, s)) * 2 > len(s) else s.lower()
#   1.  We use a functional approach to solve this problem in a single line. 
#       a.  `map(str.isupper, s)` applies the `str.isupper` function to each char in the str `s`
#           to generate a map object of booleans (True for uppercase, False for lowercase).
#       b.  `sum(...)` then sums up the number of uppercase chars in the str.
#       c.  `sum(...) * 2 > len(s)` checks if the number of uppercase chars is more than half of the 
#           length of the str.
#       d.  If the condition is true, we return the str in uppercase; otherwise, we return it in lowercase.

#   The time complexity of this solution is O(n) as it goes through each char in the str once.
#   The space complexity is O(1) as we only use a fixed amount of space to store the 
#   intermediate results albeit a little more than the previous solution temporarily for the mappping.

# -------------------------------------------------------------------------------------
# -----Solution 3-----List Comprehension-----
def solve(s):
    lower_case = [l for l in s if l.islower()]
    upper_case = [l for l in s if l.isupper()]
    
    if len(upper_case) > len(lower_case):
        return s.upper()
    return s.lower()
#   1.  We use list comprehension to create two lists, `lower_case` and `upper_case`, 
#       containing the lowercase and uppercase chars in the str `s`, respectively.
#   2.  We then compare the lengths of the two lists.
#       a.  If the length of `upper_case` is greater than the length of `lower_case`, 
#           we return the str in uppercase.
#       b.  Otherwise, we return the str in lowercase.

#   The time complexity of this solution is O(n) as it goes through each char in the str once.
#   The space complexity is potentially O(n) as we create two lists that could potentially store 
#   all the chars in the str.

# -------------------------------------------------------------------------------------
# -----Solution 4-----Javascript Solution-----Counting w/ For Loop-----
# function solve(s){
#     let lowerC = 0;
#     let upperC = 0;
#     for( let i = 0;i<s.length;i++){
#       if( s[i] == s[i].toUpperCase()){
#         upperC++;
#       }
#       else{
#         lowerC++;
#       }
#     }
#     return lowerC >= upperC ? s.toLowerCase() : s.toUpperCase()
# }

#   This is the same as Solution 1 but in Javascript. The time and space complexities are the same.
#   It starts by iterating through each char in the str and counting the number of uppercase and 
#   lowercase chars. It then compares the counts and returns the str in lowercase if the number of 
#   lowercase chars is greater than or equal to the number of uppercase chars; otherwise, it returns 
#   the str in uppercase.