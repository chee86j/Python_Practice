# Simple Encryption #1 - Alternating Split

# Implement a pseudo-encryption algorithm which given a string S and 
# an integer N concatenates all the odd-indexed characters of S with 
# all the even-indexed characters of S, this process should be 
# repeated N times.

# Examples:

# encrypt("012345", 1)  =>  "135024"
# encrypt("012345", 2)  =>  "135024"  ->  "304152"
# encrypt("012345", 3)  =>  "135024"  ->  "304152"  ->  "012345"

# encrypt("01234", 1)  =>  "13024"
# encrypt("01234", 2)  =>  "13024"  ->  "32104"
# encrypt("01234", 3)  =>  "13024"  ->  "32104"  ->  "20314"
# Together with the encryption function, you should also implement a 
# decryption function which reverses the process.

# If the string S is an empty value or the integer N is not positive, 
# return the first argument without changes.

# -------------------------------------------------------------------------------------
# -----Solution 1-----List Slicing, For Loop, Join, Range, Join-----
def decrypt(text, n):
    if text in ("", None):
        return text
    
    ndx = len(text) // 2

    for i in range(n):
        a = text[:ndx]
        b = text[ndx:]
        text = "".join(b[i:i+1] + a[i:i+1] for i in range(ndx + 1))
    return text

#   1.  Create a () that takes in two arguments, text and n
#   2.  Check if text is an empty string or None
#   3.  Return text
#   4.  Create a var ndx and set it to length of text divided by 2
#   5.  Create a for loop that will iterate through range of n
#   6.  Create a var a and set it to first half of text
#   7.  Create a var b and set it to second half of text
#   8.  Set text to concatenation of b[i:i+1] and a[i:i+1] for i in range of ndx + 1
#   9.  Return text

#   The solution in Solution 1 basically takes the first half of the text and sets it to a,
#   and the second half of the text and sets it to b.
#   It then sets text to concatenation of b[i:i+1] and a[i:i+1] for i in range of ndx + 1.
#   This will alternate the characters in the text based on the value of n.

# -------------------------------------------------------------------------------------
# -----Solution 2-----Same as Solution 1, but with List Comprehension-----
def encrypt(text, n):
    for i in range(n):
        text = text[1::2] + text[::2]
    return text


def decrypt(s, n):
    if not s: return s
    o, l = len(s) // 2, list(s)
    for _ in range(n):
        l[1::2], l[::2] = l[:o], l[o:]
    return ''.join(l)


def encrypt(s, n):
    if not s: return s
    for _ in range(n):
        s = s[1::2] + s[::2]
    return s

#   1.  Create a () that takes in two arguments, s and n
#   2.  Check if s is an empty string
#   3.  Return s
#   4.  Create a var o and set it to length of s divided by 2
#   5.  Create a list l and set it to list of s
#   6.  Create a for loop that will iterate through range of n
#   7.  Set odd-indexed elements of l to first half of l
#   8.  Set even-indexed elements of l to second half of l
#   9.  Return concatenated elements of l
#   10. Create a for loop that will iterate through range of n
#   11. Set s to concatenation of odd-indexed elements of s and even-indexed elements of s
#   12. Return s

#   The solution in Solution 2 basically takes the first half of the text and sets it to a, 
#   and the second half of the text and sets it to b. It then sets text to concatenation of
#   b[i:i+1] and a[i:i+1] for i in range of ndx + 1. This will alternate the characters in
#   the text based on the value of n.
#   It differs from Solution 1 in that it uses list comprehension to set the values of a 
#   and b as well as to set the value of text.

