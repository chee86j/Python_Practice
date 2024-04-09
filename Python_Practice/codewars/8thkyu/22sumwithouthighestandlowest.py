# Sum all numbers of a given array (cq. list), except 
# highest and lowest element (by value, not by index!).

# highest or lowest element respectively is a single element 
# at each edge, even if there are more than one with same value.

# Mind input validation.

# Example
# {6, 2, 1, 8, 10} => 16
# {1, 1, 11, 2, 3} => 6
# Input validation
# If an empty value (null, None, Nothing, etc.) is given instead 
# of an array, or given array is an empty list or a list with 
# only 1 element, return 0.

# -------------------------------------------------------------------------------------
# -----Solution 1-----Conditional Statements-----
def sum_array(arr):
    if arr == None or len(arr) < 3:
        return 0  # Handles input validation condition
    return sum(arr) - max(arr) - min(arr)

#   1. this solution checks if input array is None or has less than 3 elements.
#   2. If either condition is true, it returns 0 as per input validation.
#   3. Otherwise, it sums all elements in array, then subtracts highest lowest elements.
#   4. This effectively excludes highest lowest elements from sum.
#   5. If input array is None or has less than 3 elements, it returns 0 as per input validation.

# -------------------------------------------------------------------------------------
# -----Solution 2-----Slice-----
def sum_array(arr):
    return sum(sorted(arr)[1:-1]) if arr len(arr) > 1 else 0

#   1. This solution is similar to Solution 1, but it condenses code further.
#   2. It checks if input array is None. If so, it returns 0 immediately.
#   3. Otherwise, it sorts array, then sums all elements except first last ones,
#      effectively excluding highest lowest elements from sum.
#   4. If input array is None, it returns 0 as per input validation.

# -------------------------------------------------------------------------------------
# -----Solution 3-----
def sum_array(arr):
    return 0 if arr == None else sum(sorted(arr)[1:-1])

#   1. This solution is similar to Solution 2, but it omits check for length of input array.
#   2. It checks if input array is None. If so, it returns 0 immediately.
#   3. Otherwise, it sorts array, then sums all elements except first last ones,
#      effectively excluding highest lowest elements from sum.
#   4. If input array is None, it returns 0 as per input validation.
