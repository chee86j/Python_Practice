# Given a positive number n > 1 find the prime factor 
# decomposition of n. The result will be a string with the following form :

#  "(p1**n1)(p2**n2)...(pk**nk)"

# with the p(i) in increasing order and n(i) empty if n(i) is 1.

# Example: n = 86240 should return "(2**5)(5)(7**2)(11)"

# -------------------------------------------------------------------------------------
# -----My Notes----
#   You are required for finding the prime factor decomposition of a given positive 
#   integer `n` that is greater than 1. The prime factor decomposition of a number `n`
#   as a product of its prime factors, where each prime factor is raised to the power
#   of the number of times it divides `n`. 

#   You should express `n` as a product of its prime factors with the following format:
#   "(p1**n1)(p2**n2)...(pk**nk)" where `p(i)` is the `i-th` prime factor of `n` and
#   `n(i)` is the number of times `p(i)` divides `n`. 

# -------------------------------------------------------------------------------------
# -----Solution 1----While loop & if/elif/else----Easy to Follow----
def primeFactors(n):
    i = 2
    r = ''
    while n != 1:
        k = 0
        while n%i == 0:
            n = n / i
            k += 1
        if k == 1:
            r = r + '(' + str(i) + ')'
        elif k == 0: pass
        else:
            r = r + '(' + str(i) + '**' + str(k) + ')'
        i += 1
        
    return r
#   1. Initialize i to 2 & r to an empty str
#   2. While n is not equal to 1, do the following:
#       a. Initialize k to 0
#       b. While n is divisible by i, do the following:
#           i. Divide n by i
#           ii. Increment k by 1
#       c. If k is equal to 1, add the str representation of i to r
#       d. Else if k is equal to 0, do nothing
#       e. Else, add the str representation of i, '**', & k to r
#       f. Increment i by 1
#   3. Return r
#   
#   This function uses a while loop to find the prime factors of n. 
#   It iterate through each number from 2 to n to check if it is a factor of n. 
#   If `i` is a factor of `n`, it divides `n` by `i` & increments the 
#   count of `i` in the result str. Else, it moves on to the next number. 
#   
#   The time complexity of this solution is O(n) because it iterates through 
#   each number from 2 to n to find the prime factors of n. It has a space 
#   complexity of O(1) because it uses a constant amount of extra space to 
#   store the result str. It is not efficient for larger `n` values, because 
#   it iterates through all numbers up to `n` to find the prime factors, even
#   after `n` has been divided by smaller prime factors. In terms of readability, 
#   this solution is very straightforward to understand step by step.

# -------------------------------------------------------------------------------------
# -----Solution 2----List comprehension & while loop & join----Slightly More Efficient----
def primeFactors(n):
    i, j, p = 2, 0, []
    while n > 1:
        while n % i == 0: n, j = n / i, j + 1
        if j > 0: p.append([i,j])
        i, j = i + 1, 0
    return ''.join('(%d' %q[0] + ('**%d' %q[1]) * (q[1] > 1) + ')' for q in p)
#   1. Initialize i, j, & p to 2, 0, & an empty list respectively
#   2. While n is greater than 1, do the following:
#       a. While n is divisible by i, do the following:
#           i. Divide n by i
#           ii. Increment j by 1
#       b. If j is greater than 0, append a list containing i & j to p
#       c. Increment i by 1 & reset j to 0
#   3. Return a str created by joining the elements of a list comprehension
#       a. For each element q in p, do the following:
#           i. Create a str containing i
#           ii. If j is greater than 1, add '**' & j to the str
#           iii. Add ')' to the str
#   4. Return the joined str

#   Just like solution 1, this function uses a while loop to find the prime factors of n,
#   by iterating through possible divisors but uses a list `p` to store the prime factors &
#   their counts. This lists is then uses to generate the final str result. 
#   The time complexity of this solution is O(n) because it iterates through each number
#   from 2 to n to find the prime factors of n. It has a space complexity of O(n) because
#   it uses a list to store the prime factors & their counts. This solution is more efficient
#   than solution 1 because it only stores the prime factors & their counts, rather than
#   storing the result str. In terms of readability, this solution is more concise using
#   list comprehension to generate the result str, but may be less straightforward to
#   understand.

# -------------------------------------------------------------------------------------
# -----Solution 3----Most Efficient w/ While Loop----
def primeFactors(n):
  result = ''
  fac = 2
  while fac <= n:
    count = 0
    while n % fac == 0:
      n /= fac
      count += 1
    if count:
      result += '(%d%s)' % (fac, '**%d' % count if count > 1 else '')
    fac += 1
  return result
#   1. Initialize result to an empty str & fac to 2
#   2. While fac is less than or equal to n, do the following:
#       a. Initialize count to 0
#       b. While n is divisible by fac, do the following:
#           i. Divide n by fac
#           ii. Increment count by 1
#       c. If count is not 0, add a str to result
#           i. The str contains fac
#           ii. If count is greater than 1, add '**' & count to the str
#   3. Increment fac by 1
#   4. Return result

#   This function is similar to solution 1, but uses a more concise way to 
#   generate the result str. It uses a while loop to find the prime factors 
#   of n, by iterating through possible divisors. It then generates the result
#   str directly by appending to the result str. The time complexity of
#   this solution is O(n) because it iterates through each number from 2 to n
#   to find the prime factors of n. It has a space complexity of O(1) because
#   it uses a constant amount of extra space to store the result str. This
#   solution is more efficient than solution 1 because it generates the result
#   str directly, rather than storing intermediate results. Just slightly
#   more optimized than solution 1. This is probably the most efficient solution
#   for this problem because it stops iterationg early when possible.

# -------------------------------------------------------------------------------------
# -----Solution 4----Javascript Solution----For Loop & While Loop----
# function primeFactors(n){
#   for (var i=2, res="", f; i <= n; i++) {
#     f=0;
#     while (n%i == 0) { f++; n/=i }
#     res += f ? "(" + ( f>1 ? i+"**"+f  : i ) +")" : ""
#   }
#   return res || "("+n+")"
# }
#   1. Initialize i to 2, res to an empty str, & f to undefined
#   2. Loop through each number from 2 to n
#       a. Initialize f to 0
#       b. While n is divisible by i, do the following:
#           i. Increment f by 1
#           ii. Divide n by i
#       c. If f is not 0, add a str to res
#           i. The str contains i
#           ii. If f is greater than 1, add '**' & f to the str
#   3. Return res if it is not an empty str, else return a str containing n

#   This function is similar to solution 3, but uses a for loop instead of a while loop. 
#   It generates the result str directly by appending to the result str. The time
#   complexity of this solution is O(n) because it iterates through each number from 2 to n
#   to find the prime factors of n. It has a space complexity of O(1) because it uses a
#   constant amount of extra space to store the result str. This solution is more
#   efficient than solution 1 because it generates the result str directly, rather than
#   storing intermediate results. This is probably the most efficient solution because it stops iterating early when possible.