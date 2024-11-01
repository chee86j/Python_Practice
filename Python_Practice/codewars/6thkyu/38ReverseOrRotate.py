# The input is a string str of digits. Cut the string into chunks 
# (a chunk here is a substring of the initial string) of size sz 
# (ignore the last chunk if its size is less than sz).

# If the sum of a chunk's digits is divisible by 2, reverse that 
# chunk; otherwise rotate it to the left by one position. Put 
# together these modified chunks and return the result as a string.


# If

# sz is <= 0 or if str == "" return ""
# sz is greater (>) than the length of str it is impossible to take 
# a chunk of size sz hence return "".


# Examples:

# ("123456987654", 6) --> "234561876549"
# ("123456987653", 6) --> "234561356789"
# ("66443875", 4) --> "44668753"
# ("66443875", 8) --> "64438756"
# ("664438769", 8) --> "67834466"
# ("123456779", 8) --> "23456771"
# ("", 8) --> ""
# ("123456779", 0) --> "" 
# ("563000655734469485", 4) --> "0365065073456944"


# Example of a string rotated to the left by one position:
# s = "123456" gives "234561".

# -------------------------------------------------------------------------------------
# -----Solution 1-----Helper Function w/Conditional Return & Chunking w/zip()-----
def func(s):
    result = sum(int(x)**3 for x in s)
    if result % 2 == 0:
        return s[::-1]
    else:
        return s[1:] + s[0]

def revrot(s, sz):
    if not sz:
        return ''
    return ''.join(func(''.join(x)) for x in zip(*[iter(list(s))]*sz))
    
#   1. Define a helper function func(s) that takes a string s as input.
#   2. Calculate the sum of the cubes of the digits in the string s.
#      "sum(int(x)**3 for x in s)"
#   3. Check if the sum is divisible by 2.
#   4. If the sum is divisible by 2, return the reversed string s.
#   5. If the sum is not divisible by 2, return the string s rotated to the left by one position.
#      "s[1:] + s[0]"

#   6. Define the main function revrot(s, sz) that takes a string s & an integer sz as input.
#   7. Check if sz is 0. If it is, return an empty string.
#   8. Use the zip() function to group the characters of the string s into chunks of size sz.
#   9. Apply the helper function func() to each chunk using a list comprehension.
#   10. Join the modified chunks together to form the final result.

#   The time complexity of this solution is O(n) where n is the length of the string s.
#   The space complexity of this solution is O(n) where n is the length of the string s.

#   In terms of efficiency, this solution may be less readable due to the zip() for chunking the string.
#   However, it is a concise & efficient way to solve the problem.


# -------------------------------------------------------------------------------------
# -----Solution 2-----
def rev_rot(strng, sz):
    list=[]
    endstring=""
    total=0
    if sz<=0:
        return ""
    elif strng=="":
        return ""
    else:
        for x in range (len(strng)//sz):
            list.append(strng[x*sz:(x+1)*sz])
        for x in range (len(list)):
            total=0
            for y in range (len(list[x])):
                total+=int(list[x][y])**3
            if total%2==0:
                endstring+=(list[x])[::-1]
            else:
                endstring+=list[x][1:]+list[x][0]
        return endstring
#   1. Initialize an empty list to store the chunks of the string.
#   2. Initialize an empty string to store the final result.
#   3. Initialize a variable total to store the sum of the cubes of the digits in each chunk.
#   4. Check if sz is less than or equal to 0. If it is, return an empty string.
#   5. Check if the string is empty. If it is, return an empty string.
#   6. Split the string into chunks of size sz & store them in the list.
#   7. Iterate over each chunk in the list.
#   8. Calculate the sum of the cubes of the digits in the chunk.
#   9. Check if the sum is divisible by 2.
#   10. If the sum is divisible by 2, reverse the chunk & add it to the endstring.
#   11. If the sum is not divisible by 2, rotate the chunk to the left by one position & add it to the endstring.
#   12. Return the final result.

#   The time complexity of this solution is O(n) where n is the length of the string strng.
#   The space complexity of this solution is O(n) where n is the length of the string strng.

#   In terms of efficiency, this solution uses a more traditional approach to split the string into chunks
#   & process each chunk individually. It is easy to understand & implement but may be less concise
#   than the previous solution.


# -------------------------------------------------------------------------------------
# -----Solution 3-----
import re

def rev_rot(strng, sz):
    if sz <= 0 or not strng or sz > len(strng):
        return ""
    
    chunks = re.findall('.' * sz, strng)
    
    modified_chunks = [
        chunk[::-1] if sum(int(digit) for digit in chunk) % 2 == 0
        else chunk[1:] + chunk[0]
        for chunk in chunks
    ]
    
    return "".join(modified_chunks)
#   1. Check if sz is less than or equal to 0, if the string is empty, or if sz is greater 
#      than the length of the string.
#   2. If any of the conditions are met, return an empty string.
#   3. Use the re.findall() function to split the string into chunks of size sz.
#      "re.findall('.' * sz, strng)"
#   4. Iterate over each chunk & apply the modification logic.
#      "chunk[::-1]" reverses the chunk if the sum of the digits is even.
#      "chunk[1:] + chunk[0]" rotates the chunk to the left by one position if the sum of 
#      the digits is odd.
#   5. Join the modified chunks together to form the final result.

#   The time complexity of this solution is O(n) where n is the length of the string strng.
#   The space complexity of this solution is O(n) where n is the length of the string strng.

#   In terms of efficiency, compared to the previous solution, this solution uses regular 
#   expressions to split the string into chunks.
#   This can be more efficient for large strings as it avoids creating intermediate lists 
#   of chunks. However, it may be less readable.

# -------------------------------------------------------------------------------------
# -----Solution 4-----Javascript Version-----
# function revrot(str, sz) {
#     if (sz <= 0 || !str || sz > str.length) return '';    
      
#     const sumCubes = chunk => chunk.split('').reduce((sum, digit) => sum += digit**3, 0);
#     const reverse = chunk => chunk.split('').reverse().join('');
#     const rotate = chunk => chunk.slice(1) + chunk.slice(0, 1);
    
#     const chunks = [];
    
#     for (let i = 0; i < str.length; i += sz) {
#       let chunk = str.slice(i, i + sz);
      
#       if (chunk.length < sz) continue;
      
#       chunk = sumCubes(chunk) % 2 
#         ? rotate(chunk)   
#         : reverse(chunk);
      
#       chunks.push(chunk)
#     }
    
#     return chunks.join('')
# }
#   Compared to the 1st solution, this solution uses a for loop to iterate over the string & 
#   process each chunk individually.
#   It uses helper functions to calculate the sum of cubes, reverse a chunk, & rotate a chunk.
#   It also checks if the chunk length is less than sz & skips it if it is.
#   The modified chunks are stored in an array & joined together at the end to form the final result.

#   The time complexity of this solution is O(n) where n is the length of the string str.
#   The space complexity of this solution is O(n) where n is the length of the string str.
#   This solution is more efficient than the previous one as it avoids creating intermediate 
#   lists of chunks & uses helper functions for processing.
