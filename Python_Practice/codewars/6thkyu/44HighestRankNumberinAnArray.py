# Complete the method which returns the number which is most frequent in the given input 
# array. If there is a tie for most frequent number, return the largest number among them.

# Note: no empty arrays will be given.

# Examples

# [12, 10, 8, 12, 7, 6, 4, 10, 12]              -->  12
# [12, 10, 8, 12, 7, 6, 4, 10, 12, 10]          -->  12
# [12, 10, 8, 8, 3, 3, 3, 3, 2, 4, 10, 12, 10]  -->   3

# -------------------------------------------------------------------------------------
# -----Solution 1-----Using collections.Counter-----
from collections import Counter

def highest_rank(arr):
    if arr:
        c = Counter(arr)
        m = max(c.values())
        return max(k for k,v in c.items() if v==m)
#   1. Using Python's collections module, the Counter class is imported to efficiently
#      count the frequency of each element in the array.
#   2. The Counter object is created by passing the array as an argument.
#   3. The max() function is used to find the highest frequency in the Counter object.
#   4. A generator expression is used to iterate through the key-value pairs in the Counter
#      object. If the value of the current key-value pair is equal to the highest frequency,
#      the key is returned.

#   The time complexity of this solution is O(n) because the Counter object is created by
#   iterating through the array. The space complexity is also O(n) because the Counter object
#   stores the frequency of each element in the array. This solution is concise & uses
#   Python's built-in functions to find the most frequent number in the array.


# -------------------------------------------------------------------------------------
# -----Solution 2-----Sorted & arr.count-----
def highest_rank(arr):
    return max(sorted(arr,reverse=True), key=arr.count)
#   1. The sorted() function is used to sort the array in descending order.
#   2. The max() function is used to find the maximum element in the sorted array based on
#      the key function arr.count.
#   3. The key function arr.count is used to count the number of occurrences of each element
#      in the array.

#   The time complexity of this solution is O(n log n) because the sorted() function is used
#   to sort the array. The space complexity is O(1) because no additional data structures are
#   used. This solution is concise & uses Python's built-in functions to find the most
#   frequent number in the array. Compared to Solution 1, this solution is more concise &
#   uses fewer lines of code. It is less efficient for large arrays with many unique elements

# -------------------------------------------------------------------------------------
# -----Solution 3-----Usingsorting with Lambda-----
def highest_rank(arr):
    return sorted(arr,key=lambda x: (arr.count(x),x))[-1]
#   1. The sorted() function is used to sort the array based on the key function lambda x:
#      (arr.count(x), x).
#   2. The key function lambda x: (arr.count(x), x) returns a tuple of the count of the
#      element x in the array & the element x itself.
#   3. The sorted array is indexed with [-1] to return the last element, which is the
#      largest number among the most frequent numbers.

#   The time complexity of this solution is O(n log n) because the sorted() function is used
#   to sort the array. The space complexity is O(1) because no additional data structures are
#   used. This solution is concise & uses Python's built-in functions to find the most
#   frequent number in the array. Compared to Solution 1, this solution is more concise &
#   uses fewer lines of code. It is less efficient for large arrays due to repeated calls to
#   the arr.count() method.

# -------------------------------------------------------------------------------------
# -----Solution 4-----JavaScript Solution-----
# function highestRank(arr){
#   var obj = {};
#   arr.forEach(function(elem){
#      if(obj[elem] === undefined)
#        obj[elem] = 0;
#      obj[elem]++;
#   });
#   var keys = Object.keys(obj), highest = 0, key;
#   keys.forEach(function(elem){
#      if(obj[elem] >= highest)
#      {
#         highest = obj[elem];
#         key = elem;
#      }
#   })
#   return parseInt(key);
# }

#   1. An object is created to store the count of each element in the array.
#   2. The forEach() method is used to iterate through the array. If the number is
#      not in the object, it is added & set to 0. The number is then incremented.
#   3. To find the most frequent number, the keys of the object are stored in an array.
#   4. The keys of the frequency object are iterated through. If the frequency of the
#      current number is greater than or equal to the highest frequency, the highest
#      frequency is updated & the key is stored.
#   5. Finally, the key is returned as an integer.

#   The time complexity of this solution is O(n) because the forEach() method is used to
#   iterate through the array & the keys of the object. The space complexity is also O(n)
#   because an object is created to store the frequency of each element in the array.
#   It is clear & easy to follow even for beginners. It uses native JavaScript methods
#   & does not require any additional libraries.  Compared to the Python solutions, this
#   solution is more verbose & requires more lines of code. It is less efficient for large
#   arrays with many unique elements due to the repeated iteration through the array & the
#   keys of the object, but it is still an effective solution.
