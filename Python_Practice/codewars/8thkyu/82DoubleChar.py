# Given a string, you have to return a string in which each character 
# (case-sensitive) is repeated once.

# Examples (Input -> Output):
    
# * "String"      -> "SSttrriinngg"
# * "Hello World" -> "HHeelllloo  WWoorrlldd"
# * "1234!_ "     -> "11223344!!__  "

# Good Luck!

# -------------------------------------------------------------------------------------
# -----Solution 1-----Join () w/Generator Expression-----
def double_char(s):
    return ''.join(c * 2 for c in s)
#   1. This solution uses Python's join() method which is efficient for joining strings.
#   2. It iterates through each char 'c' in the string 's' & multiplies it by 2.
#   3. The generator expression '(c * 2 for c in s)' is passed to the join() method so to
#      concatenate the repeated chars into a single string.
#   4. The final string is returned.

#   The time complexity of this solution is O(n) where n is the length of the input string 's'.
#   because we perform a constant-time operation (repeating it twice) for each char in the string.
#   The space complexity is also O(n) because we create a new string of length n since we repeat
#   each char in the input string only once.

#   This solution is quite efficient as it minimizes memory usage using a generator expression
#   & leverages the efficient join() method for string concatenation.

# -------------------------------------------------------------------------------------
# -----Solution 2-----String Concatenation w/a For Loop-----
def double_char(s):
    res = ''
    for i in s:
        res += i*2
    return res
#   1. This solution uses a for loop to iterate through each char 'i' in the input string 's'.
#   2. For each char 'i', we multiply it by 2 & concatenate it to the result string 'res'.
#   3. The final result string 'res' is returned.

#   The time complexity of this solution is O(n) where n is the length of the input string 's'.
#   because we perform a constant-time operation (repeating it twice) for each char in the string.
#   The space complexity is also O(n) because we create a new string of length n since we repeat
#   each char in the input string only once.

#   This is not as efficient compared to the first solution because we use the '+=' operator in 
#   Python because strings are immutable. This means that each time we concatenate a char to the
#   result string, Python creates a new string object to store the result. This can be inefficient
#   when dealing with large strings.

# -------------------------------------------------------------------------------------
# -----Solution 3-----Using List & Manual String Concatenation-----
def double_char(s):
    y = list(s)
    length = len(y)
    ffs = list(range(0,length))
    blank=""
    
    for i in ffs:
        blank = blank + y[i] + y[i]
    return blank
#   1. This solution first converts the input string 's' into a list 'y'.
#   2. It then constructs a range of indices 'ffs' from 0 to the length of the list 'y'.
#   3. It initializes an empty string 'blank' to store the final result.
#   4. It then iterates through the range of indices 'ffs' & concatenates each char in the list
#      'y' to the result string 'blank' by multiplying it by 2.
#   5. The final result string 'blank' is returned.

#   The time complexity of this solution is O(n) where n is the length of the input string 's'.
#   because we perform a constant-time operation (repeating it twice) for each char in the string.
#   The space complexity is also O(n) because we create a new string of length n since we repeat
#   each char in the input string only once.

#   This solution is less efficient compared to the first solution because we manually concatenate
#   each char to the result string 'blank' using the '+' operator. This can be inefficient when
#   dealing with large strings.

# -------------------------------------------------------------------------------------
# -----Solution 4-----JavaScript Solution-----
# const doubleChar = (str) => str.split("").map(c => c + c).join("");
# 1. This solution uses JavaScript's split() method to convert the input string 'str' into an array of chars.
# 2. It then uses the map() method to iterate through each char 'c' in the array & multiplies it by 2.
# 3. The join() method is used to concatenate the repeated chars into a single string.
# 4. The final string is returned.

# The time complexity of this solution is O(n) where n is the length of the input string 'str'.
# because we perform a constant-time operation (repeating it twice) for each char in the string.
# The space complexity is also O(n) because we create a new string of length n since we repeat
# each char in the input string only once.

# This solution is quite efficient as it minimizes memory usage using the map() method & leverages
# the efficient join() method for string concatenation. It is similar to the first Python solution.
