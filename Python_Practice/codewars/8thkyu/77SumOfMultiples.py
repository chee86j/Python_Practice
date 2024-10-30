# Your Job
# Find the sum of all multiples of n below m

# Keep in Mind
# n and m are natural numbers (positive integers)
# m is excluded from the multiples

# Examples
# sumMul(2, 9)   ==> 2 + 4 + 6 + 8 = 20
# sumMul(3, 13)  ==> 3 + 6 + 9 + 12 = 30
# sumMul(4, 123) ==> 4 + 8 + 12 + ... = 1860
# sumMul(4, -7)  ==> "INVALID"

# -------------------------------------------------------------------------------------
# -----Solution 1-----range() and sum() w/Vaildation-----
def sum_mul(n, m):
    if m>0 and n>0:
        return sum(range(n, m, n))
    else:
        return 'INVALID'
#   1. Check if m and n are positive integers.
#   2. If they are, use the range() function to generate a list of multiples of n from n to m.
#   3. Use the sum() function to calculate the sum of the list of multiples.
#   4. Return the sum if m and n are positive integers, otherwise return 'INVALID'.

#   The time complexity of this solution is O(n) where n is the number of multiples between n and m.
#   The space complexity of this solution is O(n) where n is the number of multiples between n and m.



# -------------------------------------------------------------------------------------
# -----Solution 2-----Generator Expresssion w/Conditional Check-----
def sum_mul(n, m):
    return sum(x for x in range(n, m, n)) if m > 0 and n > 0 else 'INVALID'
#   1. Check if m and n are positive integers.
#   2. Use a generator expression to generate multiples of n from n to m.
#   3. Use the sum() function to calculate the sum of the generator expression.
#   4. Return the sum if m and n are positive integers, otherwise return 'INVALID'.

#   The time complexity of this solution is O(n) where n is the number of multiples between n and m.
#   The space complexity of this solution is O(n) where n is the number of multiples between n and m.

#   Compared to Solution 1, this solution uses a generator expression instead of the range() function 
#   to generate the list of multiples. This can be more memory-efficient as it generates the multiples 
#   on-the-fly instead of creating a list in memory. However, the time complexity remains the same as 
#   the number of multiples generated is the same in both cases. This is better for large ranges.

# -------------------------------------------------------------------------------------
# -----Solution 3-----Ternary w/Validation Before range()-----
def sum_mul(n, m):
    return sum(range(n, m, n)) if n > 0 and m > 0 else "INVALID"
#   1. Check if n and m are positive integers.
#   2. If they are, use the range() function to generate a list of multiples of n from n to m.
#   3. Use the sum() function to calculate the sum of the list of multiples.
#   4. Return the sum if n and m are positive integers, otherwise return 'INVALID'.

#   The time complexity of this solution is O(n) where n is the number of multiples between n and m.
#   The space complexity of this solution is O(n) where n is the number of multiples between n and m.

#   This solution is similar to Solution 1 but with the validation check before generating the list of multiples.
#   It is slightly more capable than Solution 2 as it avoids generating the list of multiples if the input is invalid.

# -------------------------------------------------------------------------------------
# -----Solution 4-----Javascript Version-----Looping w/Vaildation-----
# function sumMul(n,m){
#   if (n >= m) return "INVALID";

# var sum = 0;
#   for (var i = n; i < m; i+=n) {
#     sum += i;
#   }
#   return sum;
# }
#   1. Check if n is greater than or equal to m. If it is, return "INVALID".
#   2. Initialize a variable sum to 0.
#   3. Use a for loop to iterate from n to m with a step size of n.
#   4. Add each multiple of n to the sum.
#   5. Return the sum.

#   The time complexity of this solution is O(n) where n is the number of multiples between n and m.
#   The space complexity of this solution is O(1) as it only uses a constant amount of space.
