# DESCRIPTION:
# Well met with Fibonacci bigger brother, AKA Tribonacci.

# As the name may already reveal, it works basically like a Fibonacci, 
# but summing the last 3 (instead of 2) numbers of the sequence to 
# generate the next. And, worse part of it, regrettably I won't get 
# to hear non-native Italian speakers trying to pronounce it :(

# So, if we are to start our Tribonacci sequence with [1, 1, 1] as a 
# starting input (AKA signature), we have this sequence:

# [1, 1 ,1, 3, 5, 9, 17, 31, ...]
# But what if we started with [0, 0, 1] as a signature? As starting 
# with [0, 1] instead of [1, 1] basically shifts the common Fibonacci 
# sequence by once place, you may be tempted to think that we would get 
# the same sequence shifted by 2 places, but that is not the case and 
# we would get:

# [0, 0, 1, 1, 2, 4, 7, 13, 24, ...]
# Well, you may have guessed it by now, but to be clear: you need to
# create a fibonacci function that given a signature array/list, returns 
# the first n elements - signature included of the so seeded sequence.

# Signature will always contain 3 numbers; n will always be a non-negative 
# number; if n == 0, then return an empty array (except in C return NULL) 
# and be ready for anything else which is not clearly specified ;)

# -------------------------------------------------------------------------------------
# -----Solution 1-----For Loop, Append, Sum-----
def tribonacci(signature, n):
  res = signature[:n]
  for i in range(n - 3): res.append(sum(res[-3:]))
  return res
#   1.  Create a function that takes in two arguments, signature and n
#   2.  Create a variable res that will store the first n elements of the signature
#   3.  Create a for loop that will iterate through the range of n - 3
#   4.  Append the sum of the last 3 elements of res to res
#   5.  Return res

# -------------------------------------------------------------------------------------
# -----Solution 2-----While Loop, Append, Sum-----
def tribonacci(signature,n):
    while len(signature) < n:
        signature.append(sum(signature[-3:]))
    
    return signature[:n]
#   1.  Create a function that takes in two arguments, signature and n
#   2.  Create a while loop that will run as long as length of signature is less than n
#   3.  Append sum of last 3 elements of signature to signature
#   4.  Return first n elements of signature

# -------------------------------------------------------------------------------------
# -----Solution 3-----For Loop, Append, Sum-----
def tribonacci(s, n):
    for i in range(3, n): s.append(s[i-1] + s[i-2] + s[i-3])
    return s[:n]
#   1.  Create a function that takes in two arguments, s and n
#   2.  Create a for loop that will iterate through range of 3 to n
#   3.  Append sum of last 3 elements of s to s
#   4.  Return first n elements of s