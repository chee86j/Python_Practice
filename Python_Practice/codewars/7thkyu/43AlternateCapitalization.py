# Given a string, capitalize the letters that occupy even indexes 
# and odd indexes separately, and return as shown below. Index 0 
# will be considered even.

# For example, capitalize("abcdef") = ['AbCdEf', 'aBcDeF']. See 
# test cases for more examples.

# Sample Test:
#     import codewars_test as test
# from solution import capitalize

# @test.describe("Fixed Tests")
# def fixed_tests():
#     @test.it('Basic Test Cases')
#     def basic_test_cases():
#         test.assert_equals(capitalize("abcdef"),['AbCdEf', 'aBcDeF'])
#         test.assert_equals(capitalize("codewars"),['CoDeWaRs', 'cOdEwArS'])
#         test.assert_equals(capitalize("abracadabra"),['AbRaCaDaBrA', 'aBrAcAdAbRa'])
#         test.assert_equals(capitalize("codewarriors"),['CoDeWaRrIoRs', 'cOdEwArRiOrS'])
#         test.assert_equals(capitalize("indexinglessons"),['InDeXiNgLeSsOnS', 'iNdExInGlEsSoNs'])
#         test.assert_equals(capitalize("codingisafunactivity"),['CoDiNgIsAfUnAcTiViTy', 'cOdInGiSaFuNaCtIvItY'])

# The input will be a lowercase string with no spaces.

# Good luck!

# -------------------------------------------------------------------------------------
# -----Solution 1----Swapcase() & Enumerate() & Join() & List Comprehension----
def capitalize(s):
    s = ''.join(c if i%2 else c.upper() for i,c in enumerate(s))
    return [s, s.swapcase()]
#   1. The string s is created by iterating over the characters of the input string s 
#      & using the ternary operator to check if the index i is even or odd.
#   2. If the index i is even, we add the character c to the string s in uppercase, 
#      otherwise we add the character c to the string s as is.
#   3. The string s with swapped cases is created by using the swapcase() on 
#      the string s.
#   4. Finally, we return a list containing the original string s & the string s with 
#      swapped cases.This has a time complexity of O(n) where n is the length of the 
#      input string s & a space complexity of O(n) as well.

# -----Python Methods-------------------------------------------------------------------
#   1. enumerate() adds a counter to an iterable & returns it in a form of 
#      enumerate object.
#   2. swapcase() is used to swap the cases of string i.e., upper case is 
#      converted to lower case & vice versa.
#   3. List comprehension is an elegant way to define & create list in Python.
#   4. join() method returns a string concatenated with the elements of an iterable.
#   5. upper() method returns a string where all characters are in upper case.
#   6. for loop `for i,c in enumerate(s)` is used to iterate over the characters of the 
#      input string s.


# -------------------------------------------------------------------------------------
# -----Solution 2----Enumerate() & List Comprehension----
def capitalize(s):
    result = ['','']
    for i,c in enumerate(s):
        result[0] += c.lower() if i % 2 else c.upper()
        result[1] += c.upper() if i % 2 else c.lower()
    return result
#   1. The result list is initialized with two empty strings.
#   2. We iterate over the characters of the input string s using the enumerate().
#   3. We use the ternary operator to check if the index i is even or odd.
#   4. If the index i is even, we add the character c to the first string in uppercase & 
#      to the second string in lowercase. `result[0] += c.lower() if i % 2 else c.upper()`
#   5. If the index i is odd, we add the character c to the first string in lowercase &
#      to the second string in uppercase. `result[1] += c.upper() if i % 2 else c.lower()`
#   6. Finally, we return the result list containing the two strings. This has a time
#      complexity of O(n) where n is the length of the input string s & a space
#      complexity of O(n) as well.
#   Compared with Solution 1, this solution is more readable & easier to understand.


# -------------------------------------------------------------------------------------
# -----Solution 3----For Loop & Swapcase() & Append()----
def capitalize(s):
    word = ""
    output = []
    for n in range(0, len(s)):
      if n%2==0:
        word = word+s[n].upper()
      else:
        word = word+s[n]
    output.append(word)
    output.append(word.swapcase())
    return output
#   1. Initialize an empty string word & an empty list output. `word = ""` & `output = []`
#   2. Iterate over the range of the length of the input string s. `for n in range(0, len(s))`
#   3. If the index n is even, we add the character s[n] to the string word in uppercase. `word = word+s[n].upper()`
#   4. If the index n is odd, we add the character s[n] to the string word as is. `word = word+s[n]`
#   5. Append the string word to the output list. `output.append(word)`
#   6. Append the string word with swapped cases to the output list. `output.append(word.swapcase())`
#   7. Finally, we return the output list. This has a time complexity of O(n) where n is the 
#      length of the input string s & a space complexity of O(n) as well.
#   Compared with Solution 1 & 2, this solution is less efficient as it uses an additional
#   list output to store the strings & is also less readable & harder to understand. 


# -------------------------------------------------------------------------------------
# -----Solution 4----Javascript Solution----Single For Loop----
# function capitalize(s) {
#   let odd = "";
#   let even = "";
  
#   for (let i = 0; i < s.length; i++) {
#     if (i % 2 === 0) {
#       even += s[i].toUpperCase();
#       odd += s[i].toLowerCase();
#     } else {
#       even += s[i].toLowerCase();
#       odd += s[i].toUpperCase();
#     }
#   }
  
#   return [even, odd];
# }
#   1. Initialize two empty strings odd & even.`let odd = ""` & `let even = ""`
#   2. Iterate over the characters of the input string s using a for loop. `for (let i = 0; i < s.length; i++)`
#   3. If the index i is even, we add the character s[i] to the string even in uppercase & to the string odd in lowercase.
#   4. If the index i is odd, we add the character s[i] to the string even in lowercase & to the string odd in uppercase.
#   5. Finally, we return an array containing the two strings even & odd.
#   This has a time complexity of O(n) where n is the length of the input string s & a space complexity of O(n) as well.
#   Compared with Solution 1, this solution is more readable & easier to understand.