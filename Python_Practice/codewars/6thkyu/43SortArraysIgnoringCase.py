# Sort the given array of strings in alphabetical order, case insensitive. For example:

# ["Hello", "there", "I'm", "fine"]  -->  ["fine", "Hello", "I'm", "there"]
# ["C", "d", "a", "B"])              -->  ["a", "B", "C", "d"]

# -------------------------------------------------------------------------------------
# -----Solution 1-----Most Pythonic Solution-----
def sortme(words):
    return sorted(words, key=str.lower)
#   1. sorted() in Python is similar to JS's sort() method, but products a new arr
#   2. Here we are sorting the words array, but we are using the key parameter to 
#      sort the array based on the lowercase version of the string, which will make
#      the sorting case insensitive.

#   The time complexity of this solution is O(nlogn), where n is the number of strings
#   in the input array. The space complexity is O(n), as sorted() will create a new
#   list.

#   This solution is the most Pythonic way to solve this problem, as it is concise and
#   easy to read. It is also efficient, as it uses the built-in sorted() function to
#   sort the array.

# -------------------------------------------------------------------------------------
# -----Solution 2-----Sorted with lambda-----
def sortme(words):
    return sorted(words,key=lambda x: x.lower())
#   1. Here we are using a lambda function to sort the array based on the lowercase
#      version of the string.
#   2. The lambda function takes a string x as input and returns x.lower(), which
#      converts the string to lowercase. Similar to => x => x.toLowerCase() in JS.

#   The time and space complexity of this solution is the same as the previous solution.
#   This is almost identical to the 1st solution, but uses a lambda function instead of
#   making it less readable.

# -------------------------------------------------------------------------------------
# -----Solution 3-----UsingSorted with str.casefold-----
def sortme(words): 
    return sorted(words,key=str.casefold)
#   1. Here str.casefold is used as the key function to sort the array. Casefold is more
#      powerful than lower() as it can handle more complex cases, such as the German 
#      ß character.

#   The time and space complexity of this solution is the same as the previous solutions as
#   well.

#   In terms of efficiency, this solution is similar to the previous ones, but it is more
#   robust when dealing with different languages and special characters. 

# -------------------------------------------------------------------------------------
# -----Solution 4-----JavaScript Solution-----
# // input: names - unsorted strings
# // output: case-agnostic sort

# sortme = function( names ){
#   return names.sort(function(first, second) {
#     return first.toLowerCase().localeCompare(second.toLowerCase())
#   })
# }

#   1. This uses JS's sort() method with a custom comparator function that:
#      a. Converts the strings to lowercase using toLowerCase().
#      b. Compares the strings using localeCompare() to handle special characters.
#   2. We start off by converting the strings to lowercase with 'first.toLowerCase()' and
#      'second.toLowerCase()'.
#   3. Then we compare the lowercase strings using 'localeCompare()', which is a more
#      powerful comparison function that can handle special characters and different
#      languages.

#   The time complexity of this solution is O(nlogn), where n is the number of strings
#   in the input array. The space complexity is O(1), as we are sorting the input array
#   in-place.
