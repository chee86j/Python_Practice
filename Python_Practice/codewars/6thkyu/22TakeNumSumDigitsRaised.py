# The number 89 is the first integer with more than one digit that 
# fulfills the property partially introduced in the title of this kata.
# What's the use of saying "Eureka"? Because this sum gives the same number: 
# 89 = 8^1 + 9^2
 

# The next number in having this property is 135:

# See this property again: 
# 135 = 1^1 + 3^2 + 5^3
 

# Task
# We need a function to collect these numbers, that may receive two integers 
# a, b that defines the range [a, b] (inclusive) and outputs a list of the sorted
# numbers in the range that fulfills the property described above.

# Examples
# Let's see some cases (input -> output):

# 1, 10  --> [1, 2, 3, 4, 5, 6, 7, 8, 9]
# 1, 100 --> [1, 2, 3, 4, 5, 6, 7, 8, 9, 89]

# If there are no numbers of this kind in the range [a, b] the function should
# output an empty list.

# 90, 100 --> []

# -------------------------------------------------------------------------------------
# -----Solution 1-----Enumerate & Sum & List Comprehension & Range & If-----
def dig_pow(n):
    return sum(int(x)**y for y,x in enumerate(str(n), 1))

def sum_dig_pow(a, b): 
    return [x for x in range(a,b + 1) if x == dig_pow(x)]

#   1. Define a function dig_pow that takes in an integer n
#   2. Return the sum of the integer raised to the power of the index + 1
#   3. Define a function sum_dig_pow that takes in two integers a and b
#   4. Return a list of numbers in the range of a and b that fulfill the property
#      described in the prompt
#   5. Use list comprehension to iterate over the range of a and b
#   6. If the number is equal to the sum of the number raised to the power of the index + 1
#      add it to the list
#   7. Return the list

# -------------------------------------------------------------------------------------
# -----Solution 2-----One Liner Similar to Solution 1-----
def sum_dig_pow(a, b):
    return [i for i in range(a, b+1) if sum(int(x)**(j+1) for j, x in enumerate(str(i))) == i]
#   1. Return a list of numbers in the range of a and b that fulfill the property
#      described in the prompt
#   2. Use list comprehension to iterate over the range of a and b
#   3. If the number is equal to the sum of the number raised to the power of the index + 1
#      add it to the list
#   4. Return the list

# -------------------------------------------------------------------------------------
# -----Solution 3-----Javascript Solution-----For Loop & If-----
# function sumDigPow(a, b) {
#   var arr = [];
#   for (var i = a; i <= b; i++) {
#     var sum = 0;
#     for (var j = 0; j <= String(i).length; j++) {
#       sum += Math.pow(parseInt(String(i)[j]), j+1);  
#       if (sum == i) arr.push(i);
#     }
#   }
#   return arr;
# }

#   1. Define a function sumDigPow that takes in two integers a and b
#   2. Define an empty array arr
#   3. Iterate over the range of a and b
#   4. Define a variable sum and set it to 0
#   5. Iterate over the length of the string of i
#   6. Add the sum of the number raised to the power of the index + 1 to sum
#   7. If the sum is equal to i add it to the array
#   8. Return the array
