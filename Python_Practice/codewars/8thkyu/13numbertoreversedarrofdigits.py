# Convert number to reversed array of digits

# Given a random non-negative number, you have to return the digits of this 
# number within an array in reverse order.
# Example(Input => Output):

# 35231 => [1,3,2,5,3]
# 0 => [0]

# -------------------------------------------------------------------------------------
# -----Solution 1-----Int & For Loop & List Comprehension-----
def digitize(n):
    return [int(i) for i in str(n)[::-1]]
    # we return a list of integers, where each integer is a digit of the number n
    # use list comprehension to iterate through the string representation of n 
    # in reverse order. [::-1] is used to reverse the string representation of n, it
    # is a slice that starts at the end of the string and ends at the beginning of the
    # string, effectively reversing the string
    
# -------------------------------------------------------------------------------------
# -----Solution 2-----Map & Int & Str-----
def digitize(n):
    return map(int, str(n)[::-1])
    # we use the built-in map function to convert each character in the string 
    # representation of n to an integer and return the result

# -------------------------------------------------------------------------------------
# -----Solution 3-----Int & For Loop & List Comprehension-----
def digitize(n):
    return [int(i) for i in reversed(str(n))]
    # we return a list of integers, where each integer is a digit of the number n
    # use list comprehension to iterate through the string representation of n
    # in reverse order. reversed() is used to reverse the string representation of n
    # it returns an iterator that yields the items of the iterable in reverse order

# -------------------------------------------------------------------------------------
# -----Solution 4-----Map & Int & Str-----
def digitize(n):
    return list(map(int, str(n)[::-1]))
    # use the built-in map function to convert each character in the string
    # representation of n to an integer and return the result as a list

# -------------------------------------------------------------------------------------
# -----Solution 5-----While Loop-----
def digitize(n):
    result = []
    while n > 0:
        result.append(n % 10)
        n = n // 10
    return result
    # initialize an empty list called result
    # use a while loop to iterate through the digits of n
    # append the remainder of n divided by 10 to result
    # update n by dividing it by 10 and discarding the remainder
    # continue this process until n is 0
    # and then return the result 