# Given two integers a and b, which can be positive or negative, 
# find the sum of all the integers between and including them and 
# return it. If the two numbers are equal return a or b.

# Note: a and b are not ordered!
# Examples (a, b) --> output (explanation)

# (1, 0) --> 1 (1 + 0 = 1)
# (1, 2) --> 3 (1 + 2 = 3)
# (0, 1) --> 1 (0 + 1 = 1)
# (1, 1) --> 1 (1 since both are same)
# (-1, 0) --> -1 (-1 + 0 = -1)
# (-1, 2) --> 2 (-1 + 0 + 1 + 2 = 2)

# Your function should only return a number, not the explanation 
# about how you get that number.

# -------------------------------------------------------------------------------------
# -----Solution 1----Iterative w/ sum() & range() & min() & max()-----
def get_sum(a,b):
    return sum(range(min(a,b), max(a,b)+1))
#   1. This () takes two arguments a & b.
#   2. min(a,b) returns the smaller of the two numbers.
#   3. max(a,b) returns the larger of the two numbers.
#   4. We then add 1 to the larger number & use the sum() function to add all the numbers 
#      between the two numbers.
#   5. The sum of the numbers between the two numbers is then returned.

#   The time complexity of this solution is O(n) because the sum() function iterates through 
#   all the numbers between the two numbers. The space complexity is O(1) because we are not 
#   using any additional data structures using a constant amount of space. 

#   This is the easiest to understand because of the direct use of the sum() & range() functions. 

# -------------------------------------------------------------------------------------
# -----Solution 2-----Arithmetic w/ abs()-----
def get_sum(a, b):
    return (a + b) * (abs(a - b) + 1) // 2
#   1. This () takes two arguments a & b.
#   2. abs(a - b) returns the absolute value of the difference between a & b.
#   3. We then add 1 to the result.
#   4. We then multiply the result by the sum of a & b.
#   5. We then divide the result by 2.
#   6. The sum of the numbers between the two numbers is then returned.

#   The time complexity of this solution is O(1) because we are not iterating through any 
#   numbers. The space complexity is O(1) because we are not using any additional data 
#   structures using a constant amount of space.

#   This can be thought of as the most efficient in both time and space complexity as it
#   computes the sum in constant time and space. 

# -------------------------------------------------------------------------------------
# -----Solution 3-----
def get_sum(a,b):
    soma=0
    if a==b:
        return a
    elif a > b:
        for i in range(b,a+1):
            soma += i
        return soma
    else:
        for i in range(a,b+1):
            soma += i
        return soma
#   1. This () takes two arguments a & b.
#   2. If a is equal to b, then a is returned.
#   3. If a is greater than b, then the for loop iterates through the range of b to a+1.
#   4. The value of i is added to the variable soma.
#   5. The value of soma is then returned.
#   6. If a is less than b, then the for loop iterates through the range of a to b+1.
#   7. The value of i is added to the variable soma.
#   8. The value of soma is then returned.

#   The time complexity of this solution is O(n) because the for loop iterates through all the 
#   numbers between the two numbers. The space complexity is O(1) because we only use one
#   additional variable to store the sum of the numbers between the two numbers.

# -------------------------------------------------------------------------------------
# -----Solution 4-----Javascript Version-----Recursion-----
# const GetSum = (a, b) => {
#   let min = Math.min(a, b),
#       max = Math.max(a, b);
#   return (max - min + 1) * (min + max) / 2;
# }
#   1. This () takes two arguments a & b.
#   2. We use the Math.min() function to return the smaller of the two numbers.
#   3. We use the Math.max() function to return the larger of the two numbers.
#   4. Then subtract the smaller number from the larger number & add 1 to the result.
#   5. Multiply the result by the sum of the two numbers.
#   6. Divide the result by 2.
#   7. The sum of the numbers between the two numbers is then returned.

#   The time complexity of this solution is O(1) because we are not iterating through any 
#   numbers. The space complexity is O(1) because we are not using any additional data
#   structures using a constant amount of space.

#   Similar to solution 2, this solution is efficient in both time and space complexity as 
#   it computes the sum in constant time and space. 