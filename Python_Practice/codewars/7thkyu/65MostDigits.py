# Find the number with the most digits.

# If two numbers in the argument array have the same number of digits, return the first one in the array.

# -------------------------------------------------------------------------------------
# -----Solution 1-----Using max() & lambda-----(Not Beginner Friendly)-----
def find_longest(arr):
    return max(arr, key=lambda x: len(str(x)))
#   1. Start off by using the max() function to find the maximum value in the arr based on the key.
#   2. The key is a lambda function (anonymous function i.e. 'lambda x: x * 2' like an arrow function in JS)
#   3. The lambda function takes an argument x & returns the length of the string representation of x.
#   4. This way, max() will compare the numbers based on the length of their string representation.
#   5. The number with the longest string representation will be returned as the result.

#   The time complexity of this solution is O(n) because the max() function iterates over the arr once to 
#   find the maximum value. The space complexity is O(1) because the lambda function does not use any additional space.
#   This is very concise & leverages the built-in functionality in Python, but might be unfamiliar to beginners.


# -------------------------------------------------------------------------------------
# -----Solution 2-----Using sort() & reverse()-----
def find_longest(arr):
    arr.sort(reverse=True) 
    return arr[0]
#   1. Start off by sorting the arr in descending order using the sort() method.
#   2. The reverse=True parameter ensures that the arr is sorted in descending order.
#   3. After sorting, the first element of the arr will be the number with the most digits.
#   4. Return this first element as the result.

#   The time complexity of this solution is O(n log n) due to the sorting operation. The space complexity is O(1)
#   because the sorting is done in-place & does not require additional space. This solution is simple & easy 
#   to underst&. However, it may not be the most efficient approach for large arrs. This is less efficient
#   than the previous solution because of the custom sorting operation.


# -------------------------------------------------------------------------------------
# -----Solution 3-----Using a Manual For Loop-----Best for Beginners-----
def find_longest(arr):
    longest = arr[0]
    
    for num in arr:
        if len(str(num)) > len(str(longest)):
            longest = num
    return longest

#   1. Start off by initializing a variable longest to the first element of the arr.
#   2. Then, iterate over the arr using a for loop.
#   3. For each number in the arr, compare the length of its string representation with the length of the 
#      current longest number. If the current number has more digits, update the longest variable to that number.
#   4. After iterating through all numbers, the longest variable will contain the number with the most digits.
#   5. Return this number as the result.

#   The time complexity of this solution is O(n) because it iterates over the arr once. The space complexity is O(1)
#   because it only uses a constant amount of additional space. This solution is straightforward & easy to underst&,
#   making it suitable for beginners. It may not be as concise as the first solution, but it is efficient & effective.


# -------------------------------------------------------------------------------------
# -----Solution 4-----JavaScript Solution-----
# const findLongest = l => l
#   .reduce((a, b) => (`${b}`.length > `${a}`.length) ? b : a);
#   1. This JavaScript solution uses the reduce() method to find the number with the most digits.
#   2. The reduce() method takes a callback function that compares the length of the string representation of each number.
#   3. If the length of the current number is greater than the length of the accumulator, the current number becomes 
#      the new accumulator.
#   4. After iterating through all numbers, the accumulator will contain the number with the most digits.
#   5. This number is returned as the result.

#   This JavaScript solution is concise & leverages the reduce() method to find the longest number. It is similar
#   to the first Python solution, which uses the max() function with a lambda function. Both solutions demonstrate
#   the power of functional programming concepts in Python & JavaScript. The time complexity of this JavaScript
#   solution is O(n) due to the reduce() operation, & the space complexity is O(1) because it uses a constant amount
#   of additional space. This solution is suitable for developers familiar with JavaScript & functional programming concepts.

