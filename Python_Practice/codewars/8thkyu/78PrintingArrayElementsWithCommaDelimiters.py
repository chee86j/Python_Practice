# Input: Array of elements

# ["h","o","l","a"]

# Output: String with comma delimited elements of the array in the same order.

# "h,o,l,a"

# Note: if this seems too simple for you try the next level

# Note2: the input data can be: boolean array, array of objects, array of string 
# arrays, array of number arrays... 

# -------------------------------------------------------------------------------------
# -----Solution 1-----
def print_array(arr):
    return ','.join(map(str, arr))
# 1. The print_array() function takes an array of elements as input.
# 2. It uses the map() function to convert each element in the array to a string.
# 3. It then uses the join() method to concatenate the elements with a comma delimiter.
# 4. The final result is a string with comma-delimited elements of the array in the same order.

# This solution has a time complexity of O(n) because it uses the map() function to convert 
# each element in the array to a string, which has a linear time complexity based on the 
# length of the array. The join() method also has a time complexity of O(n) because it 
# concatenates the elements with a comma delimiter. For the space complexity, it is O(n) 
# because the resulting string grows with the size of the input array. It is a concise
# & efficient solution that uses the map() function to convert elements to strings.

# -------------------------------------------------------------------------------------
# -----Solution 2-----
def print_array(arr):
    return ','.join(str(a) for a in arr)
# 1. The print_array() function takes an array of elements as input.
# 2. It uses a generator expression to convert each element in the array to a string.
# 3. It then uses the join() method to concatenate the elements with a comma delimiter.
# 4. The final result is a string with comma-delimited elements of the array in the same order.

# This solution has a time complexity of O(n) because it uses a generator expression to convert
# each element in the array to a string, which has a linear time complexity based on the length
# of the array. The join() method also has a time complexity of O(n) because it concatenates the
# elements with a comma delimiter. For the space complexity, it is O(n) because the resulting
# string grows with the size of the input array. It is a concise & efficient solution that uses
# a generator expression to convert elements to strings. Compared to the previous solution, it is
# less efficient due to the overhead of creating a generator object.

# -------------------------------------------------------------------------------------
# -----Solution 3-----
def print_array( _a ): return ','.join([str(i) for i in _a]) 
# 1. The print_array() function takes an array of elements as input.
# 2. It uses a list comprehension to convert each element in the array to a string.
# 3. It then uses the join() method to concatenate the elements with a comma delimiter.
# 4. The final result is a string with comma-delimited elements of the array in the same order.

# This solution has a time complexity of O(n) because it uses a list comprehension to convert
# each element in the array to a string, which has a linear time complexity based on the length
# of the array. The join() method also has a time complexity of O(n) because it concatenates the
# elements with a comma delimiter. For the space complexity, it is O(n) because the resulting
# string grows with the size of the input array. It is a concise & efficient solution that uses
# a list comprehension to convert elements to strings. Compared to the previous solutions, it is
# less efficient due to the overhead of creating a list object.
