# Write a function, persistence, that takes in a positive parameter num 
# and returns its multiplicative persistence, which is the number of 
# times you must multiply the digits in num until you reach a single digit.

# For example (Input --> Output):

# 39 --> 3 (because 3*9 = 27, 2*7 = 14, 1*4 = 4 and 4 has only one digit, 
#           there are 3 multiplications)

# 999 --> 4 (because 9*9*9 = 729, 7*2*9 = 126, 1*2*6 = 12, and finally 1*2 = 2, 
#            there are 4 multiplications)

# 4 --> 0 (because 4 is already a one-digit number, there is no multiplication)

# -------------------------------------------------------------------------------------
# -----Solution 1-----Self Calling Function with Simple Loop Approach-----
def persistence(n):
    n = str(n)
    count = 0
    while len(n) > 1:
        p = 1
        for i in n:
            p *= int(i)
        n = str(p)
        count += 1
    return count

#   Self Calling Function
#   1. Convert integer n to a string.
#   2. Initialize a count variable to 0.
#   3. Loop until n has only one digit.
#   4. Initialize a product accumulator p to 1.
#   5. Iterate through each digit i in n.
#   6. Multiply the product p by the integer value of i.
#   7. Update n to the product p as a string.
#   8. Increment the count variable by 1.
#   9. Return the count variable, which represents the number of multiplications 
#      required to reach a single digit.

#   Using the example n = 695:
#   1. n = 695, count = 0
#   2. Loop 1: n = "695", p = 6 * 9 * 5 = 270, n = "270", count = 1
#   3. Loop 2: n = "270", p = 2 * 7 * 0 = 0, n = "0", count = 2
#   4. Loop 3: n = "0", (exit loop, n has only one digit)
#   5. Return count = 3

# -------------------------------------------------------------------------------------
# -----Solution 2-----Reduce & Operator.mul-----
import operator
def persistence(n):
    i = 0
    while n>=10:
        n=reduce(operator.mul,[int(x) for x in str(n)],1)
        i+=1
    return i

#   Documentation for operator.mul: https://docs.python.org/3/library/operator.html#operator.mul
#   1. Initialize a counter i to 0.
#   2. Loop until n is less than 10.
#   3. Convert n to a list of integers and multiply all the elements together using the reduce 
#      function, which multiplies the elements of the list. Operator.mul is used as the function
#      to multiply the elements by each other. For example, reduce(operator.mul, [2, 3, 4])
#      is equivalent to 2 * 3 * 4.
#   4. Update n to the result of the multiplication.
#   5. Increment the counter i by 1.
#   6. Return the count variable, which represents the number of multiplications 
#      required to reach a single digit.

#   Using the example n = 695:
#   1. n = 695, count = 0
#   2. Loop 1: n = 6 * 9 * 5 = 270, count = 1
#   3. Loop 2: n = 2 * 7 * 0 = 0, count = 2
#   4. Loop 3: n = 0, (exit loop, n has only one digit)
#   5. Return count = 3

# -------------------------------------------------------------------------------------
# -----Solution 3-----List Manipulation with Reduce & Lambda-----
def persistence(n):
    nums = [int(x) for x in str(n)]
    sist = 0
    while len(nums) > 1:
        newNum = reduce(lambda x, y: x * y, nums)
        nums = [int(x) for x in str(newNum)]
        sist = sist + 1
    return sist
#   1. Extract digits of n and store them in a list called nums.
#   2. Initialize a counter to 0.
#   3. Loop until the length of nums is greater than 1.
#   4. Calculate the product of all the elements in nums using the reduce function and 
#      a lambda function, which multiplies two numbers together. For example, 
#      reduce(lambda x, y: x * y, [2, 3, 4]) is equivalent to 2 * 3 * 4.
#   5. Convert the product to a list of integers and assign it to nums.
#   6. Increment the counter by 1.
#   7. Return the count variable, which represents the number of multiplications 
#      required to reach a single digit.

#   Using the example n = 695:
#   1. n = 695, count = 0
#   2. Loop 1: nums = [6, 9, 5], newNum = 6 * 9 * 5 = 270, nums = [2, 7, 0], count = 1
#   3. Loop 2: nums = [2, 7, 0], newNum = 2 * 7 * 0 = 0, nums = [0], count = 2
#   4. Loop 3: nums = [0], (exit loop, nums has only one digit)
#   5. Return count = 3

# -------------------------------------------------------------------------------------
# -----Solution 4-----Javascript Solution-----Functional Approach with Array Methods-----
# function persistence(num) {
#    var times = 0;
#    num = num.toString();
#    while (num.length > 1) {
#      times++;
#      num = num.split('').map(Number).reduce((a, b) => a * b).toString();
#    }
#    return times;
# }

#  1. Initialize a counter to 0.
#  2. Convert the number to a string.
#  3. Loop until the length of the string is greater than 1.
#  4. Increment the counter by 1 for each iteration.
#  5. Split the string into an array of characters, convert each character to a number,
#     multiply all the numbers together, and convert the result back to a string.
#  6. Update the string to the result of the multiplication.
#  7. Return the count variable, which represents the number of multiplications 
#     required to reach a single digit.

#  Using the example num = 695:
#  1. num = 695, count = 0
#  2. Loop 1: num = "695", times = 1, num = "270"
#  3. Loop 2: num = "270", times = 2, num = "0"
#  4. Loop 3: num = "0", (exit loop, num has only one digit)
#  5. Return count = 3

