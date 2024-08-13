# Count the number of Duplicates
# Write a function that will return the count of distinct case-insensitive 
# alphabetic characters & numeric digits that occur more than once in the 
# input string. The input string can be assumed to contain only alphabets 
# (both uppercase & lowercase) & numeric digits.

# Example
# "abcde" -> 0 # no characters repeats more than once
# "aabbcde" -> 2 # 'a' & 'b'
# "aabBcde" -> 2 # 'a' occurs twice & 'b' twice (`b` & `B`)
# "indivisibility" -> 1 # 'i' occurs six times
# "Indivisibilities" -> 2 # 'i' occurs seven times & 's' occurs twice
# "aA11" -> 2 # 'a' & '1'
# "ABBA" -> 2 # 'A' & 'B' each occur twice

# The Main problem is you need to count how many distinct characters (ignoring case) 
# appear more than once in a given string. The string contains only alphabets 
# (both uppercase and lowercase) and numeric digits.

# -------------------------------------------------------------------------------------
# -----Solution 1-----List Comprehension & Count-----
def duplicate_count(s):
  return len([c for c in set(s.lower()) if s.lower().count(c)>1])
#  This solution uses a list comprehension to iterate through the set of characters in the input string. 
#  It is less efficient for large strings (O(n^2) time complexity) & has a space complexity of O(n) due to the list created.
#  1.  The entire string gets converted to lowercase using the lower() method.
#  2.  Create a set of characters in the input string using set() to get unique characters.
#  3.  We iterate through the set of characters using a list comprehension.
#  4.  If the count of the character in the original string is greater than 1, we add it to the list.
#  5.  The length of the list is returned as the number of duplicate characters.

# -------------------------------------------------------------------------------------
# -----Solution 2-----Sets & Count-----
def duplicate_count(text):
    seen = set()
    dupes = set()
    for char in text:
        char = char.lower()
        if char in seen:
            dupes.add(char)
        seen.add(char)
    return len(dupes)
#  This solution uses a set to store characters that have been seen & another set to store duplicate characters.
#  It has a time complexity of O(n) & a space complexity of O(n) due to the sets created & is more
#  efficient than the previous solution for large strings.
#  1.  The seen set stores characters that have been seen in the input string.
#  2.  The dupes set stores characters that have been seen more than once.
#  3.  We iterate through each character in the input string.
#  4.  The character is converted to lowercase using the lower() method.
#  5.  If the character is already in the seen set, it is added to the dupes set.
#  6.  The character is then added to the seen set.
#  7.  The length of the dupes set is returned as the number of duplicate characters.

# -------------------------------------------------------------------------------------
# -----Solution 3-----Set & Count & Avoiding List Comprehension-----
def duplicate_count(text):
    count = 0
    for c in set(text.lower()):
        if text.lower().count(c) > 1:
            count += 1
    return count
#  Similar to Solution 1, this solution uses a set to iterate through unique characters in the input string.
#  It has a time complexity of O(n^2) & a space complexity of O(n) due to the set created.
#  1.  We iterate through each unique character in the input string using a set.
#  2.  If the count of the character in the original string is greater than 1, we increment the count.
#  3.  The final count is returned as the number of duplicate characters.


# -------------------------------------------------------------------------------------
# -----Solution 4-----Javascript Solution-----
# function duplicateCount(text){
#   return (text.toLowerCase().split('').sort().join('').match(/([^])\1+/g) || []).length;
# }
#  1.  The ()) duplicateCount takes in a string text.
#  2.  It returns the count of distinct case-insensitive alphabetic characters & numeric digits that occur more than once in the input string.
#  3.  The toLowerCase method is used to convert the input string to lowercase.
#  4.  The split method is used to split the string into an array of characters.
#  5.  The sort method is used to sort the array of characters.
#  6.  The join method is used to join the sorted array back into a string.
#  7.  The match method is used with a regular expression /([^])\1+/g to find all consecutive repeated characters.
#  8.  The || [] is used to handle cases where there are no repeated characters.
#  9.  The length of the resulting array is returned as the count of duplicate characters.
#  10.  This solution has a time complexity of O(n log n) due to the sorting operation & is less elegant than the Python solutions & uses more complex regular expressions.
