# Step 1: Create a function called encode() to replace all 
# the lowercase vowels in a given string with numbers 
# according to the following pattern:

# a -> 1
# e -> 2
# i -> 3
# o -> 4
# u -> 5

# For example, encode("hello") would return "h2ll4". There 
# is no need to worry about uppercase vowels in this kata.

# Step 2: Now create a function called decode() to turn the 
# numbers back into vowels according to the same pattern 
# shown above.

# For example, decode("h3 th2r2") would return "hi there".

# For the sake of simplicity, you can assume that any numbers 
# passed into the function will correspond to vowels.

# -------------------------------------------------------------------------------------
# -----Solution 1-----Mapping w/ str.maketrans() & translate()-----
def encode(s, t=str.maketrans("aeiou", "12345")):
    return s.translate(t)
    
def decode(s, t=str.maketrans("12345", "aeiou")):
    return s.translate(t)
#   This solution is deal for short & long strings. 
#   1. It uses the str.maketrans() method to create a translation table, which maps
#      each lowercase vowel to a number according to the given pattern.
#   2. The encode() function then uses the translate() method, which applies the translation
#      table to the input string & returns the encoded string so that all vowels are replaced
#      with numbers.
#   3. The decode() function follows a similar approach, but it creates a translation table
#      that maps the numbers back to vowels. It then uses the translate() method to decode the
#      input string & return the original string with vowels.

#   This solution has a time complexity of O(n) because it uses the translate() method, which
#   has a linear time complexity based on the length of the input string. The str.maketrans()
#   method also has a time complexity of O(1) because it creates a translation table with a fixed
#   size. For the space complexity, it is also O(1) because the translation tables have a fixed size
#   & do not grow with the input size. It is a concise & efficient solution that balances readability
#   & performance.

# -------------------------------------------------------------------------------------
# -----Solution 2-----CIPHER Tuple for Storing Vowels & Numbers-----
CIPHER = ("aeiou", "12345")

def encode(st):
    return st.translate(str.maketrans(CIPHER[0], CIPHER[1]))
    
def decode(st):
    return  st.translate(str.maketrans(CIPHER[1], CIPHER[0]))
#   This solution is ideal for short strings, slightly less efficient than the previous solution due
#   to having to access the CIPHER tuple multiple times. 
#   1. It uses a tuple called CIPHER to store the mapping between vowels & numbers.
#   2. The encode() function uses the str.maketrans() method to create a translation table
#      that maps each vowel to a number based on the CIPHER tuple.
#   3. It then uses the translate() method to apply the translation table to the input string
#      & return the encoded string.
#   4. The decode() function follows a similar approach but creates a translation table that
#      maps the numbers back to vowels. It then uses the translate() method to decode the input
#      string & return the original string with vowels.

#   This solution has a time complexity of O(n) because it uses the translate() method, which has
#   a linear time complexity based on the length of the input string. The str.maketrans() method also
#   has a time complexity of O(1) because it creates a translation table with a fixed size. For the space
#   complexity, it is also O(1) because the translation tables have a fixed size & do not grow with the
#   input size. It is a concise & efficient solution that uses a tuple to store the mapping between vowels
#   & numbers.

# -------------------------------------------------------------------------------------
# -----Solution 3-----Predefined Translation Tables-----
tbl1 = str.maketrans("aeiou", "12345")
tbl2 = str.maketrans("12345", "aeiou")


def encode(st):
    return st.translate(tbl1)


def decode(st):
    return st.translate(tbl2)
#   This solution is ideal for short strings, slightly less efficient than the previous solution due
#   to having to access the CIPHER tuple multiple times.
#   1. It creates two predefined translation tables using the str.maketrans() method.
#   2. The encode() function uses the first translation table to encode the input string by
#      replacing vowels with numbers.
#   3. The decode() function uses the second translation table to decode the input string by
#      replacing numbers with vowels.

#   This solution has a time complexity of O(n) because it uses the translate() method, which has
#   a linear time complexity based on the length of the input string. The str.maketrans() method also
#   has a time complexity of O(1) because it creates a translation table with a fixed size. For the space
#   complexity, it is also O(1) because the translation tables have a fixed size & do not grow with the
#   input size. It is highly efficient due to pre-creating the translation tables & reusing them for encoding
#   avoiding the need to recreate them for each function call.

# -------------------------------------------------------------------------------------
# -----Solution 4-----Javascript Solution-----Regex & Indexing
# function encode(string){
#   return string.replace(/[aeiou]/g, function (x) { return '_aeiou'.indexOf(x) });
# }

# function decode(string){
#   return string.replace(/[1-5]/g, function (x) { return '_aeiou'.charAt(x) });
# }

#   This solution uses regular expressions to match vowels or numbers in the input string.
#   It then uses a callback function to replace each match with the corresponding index or character
#   from the '_aeiou' string. The encode() function replaces vowels with numbers, while the decode()
#   function replaces numbers with vowels. It is a concise & efficient solution that leverages regular
#   expressions & indexing to perform the encoding & decoding operations.

#   While the Python translate() method provides a more direct way to perform the encoding & decoding
#   operations, this JavaScript solution demonstrates an alternative approach using regular expressions
#   & callback functions. It is a common pattern in JavaScript for handling string manipulation tasks
#   & provides a clear way to replace characters based on a pattern.