# -----Instructions-----
# Can you find the needle in the haystack?

# Write a function findNeedle() that takes an array full of junk but containing one "needle"

# After your function finds the needle it should return a message (as a string) that says:

# "found the needle at position " plus the index it found the needle, so:

# Example(Input --> Output)

# ["hay", "junk", "hay", "hay", "moreJunk", "needle", "randomJunk"] --> "found the needle at position 5"

# -------------------------------------------------------------------------------------
# -----Solution 1-----
def find_needle(haystack):
    # Use the `index` method to find the position of "needle" in the list
    # Then, use an f-string to construct the result message (Python equivalent of string literals)
    return f'found the needle at position {haystack.index("needle")}'

# -------------------------------------------------------------------------------------
# -----Solution 2-----
def find_needle(haystack):
    # Use the `index` method to find the position of "needle" in the list
    # Then, use the `format` method to construct the result message
    # the `format` method is the Python 2 equivalent of f-strings
    return 'found the needle at position {}'.format(haystack.index('needle'))

# -------------------------------------------------------------------------------------
# -----Solution 3-----
def find_needle(haystack):
    # Use the `index` method to find the position of "needle" in the list
    index = haystack.index("needle")
    
    # Construct the result message by concatenating the index to the message
    return "found the needle at position " + str(index)
