# Build a function that returns an array of integers from n to 1 where n>0.

# Example : n=5 --> [5,4,3,2,1]

# -------------------------------------------------------------------------------------
# -----Solution 1-----Using range() and list()-----
def reverseseq(n):
    # Create a list containing integers from n to 1 in reverse order
    return list(range(n, 0, -1))

# -----Solution 2-----Using range() without list comprehension-----
def reverseseq(n):
    # Return a range object containing integers from n to 1 in reverse order
    # The range object can be converted to a list if needed
    return range(n, 0, -1)

# -----Solution 3-----Using list comprehension-----
def reverse_seq(n):
    # Create a list containing integers from n to 1 in reverse order
    # Using list comprehension for concise syntax
    return [i for i in range(n, 0, -1)]
