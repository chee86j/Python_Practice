# Given a sequence of numbers, find the largest pair sum in the sequence.

# For example

# [10, 14, 2, 23, 19] -->  42 (= 23 + 19)
# [99, 2, 2, 23, 19]  --> 122 (= 99 + 23)

# Input sequence contains minimum two elements and every element is an integer.

# -------------------------------------------------------------------------------------
# -----Solution 1-----sorted() function-----
def largest_pair_sum(numbers): 
    return sum(sorted(numbers)[-2:])
#   1.  sorted(numbers) sorts the numbers in ascending order.
#   2.  sorted(numbers)[-2:] returns the last two elements of the sorted list.
#   3.  sum(sorted(numbers)[-2:]) calculates the sum of the last two elements.

#   This solution is concise and efficient, as it only requires sorting the list once.
#   It has a time complexity of O(n log n) due to the sorting operation & a space complexity of O(n).
#   This is the most efficient solution in terms of time complexity, but it may not be the most readable.

# -------------------------------------------------------------------------------------
# -----Solution 2-----heapq module-----
from heapq import nlargest

def largest_pair_sum(a):
    return sum(nlargest(2, a))
#   1.  nlargest(2, a) returns the two largest elements in the list.
#   2.  sum(nlargest(2, a)) calculates the sum of the two largest elements.

#   This solution is efficient as it uses the nlargest function from the heapq module.
#   It has a time complexity of O(n log k) where k is the number of elements to retrieve.
#   In this case, k = 2, so the time complexity is effectively O(n log 2) = O(n).
#   Compared to the first solution, this solution is more readable and easier to understand, but
#   it requires importing the heapq module.

# -------------------------------------------------------------------------------------
# -----Solution 3-----modifying the input list w/ max() & remove()-----
def largest_pair_sum(numbers): 
    max1 = max(numbers)
    numbers.remove(max1)
    max2 = max(numbers)
    return max1 + max2
#   1.  max(numbers) returns the largest element in the list.
#   2.  numbers.remove(max1) removes the largest element from the list.
#   3.  max(numbers) returns the new largest element in the modified list.
#   4.  max1 + max2 calculates the sum of the two largest elements.
#   This solution is straightforward and easy to understand. It has a time complexity of O(n)
#   as it iterates through the list twice to find the two largest elements & space complexity of O(1).

#   However, it modifies the input list, which may not be desirable in some cases.
#   Compared to the other solutions, this solution is less efficient as it requires iterating
#   through the list twice to find the two largest elements.

# -------------------------------------------------------------------------------------
# -----Solution 4-----Javascript Solution-----
# function largestPairSum(numbers){
#   numbers.sort(function(a, b){ return b - a });
#   return numbers[0] + numbers[1];
# }
#   1.  This is the same as the third solution, but written in JavaScript. 
#   2.  It starts by sorting the numbers in descending order using a custom comparison function.
#   3.  It then returns the sum of the first two elements in the sorted array.

#   The sort method is used with a custom comparison function to sort the numbers in descending order.
#   This solution is efficient and easy to understand having a time complexity of O(n log n) 
#   due to the sorting operation & a space complexity of O(1).

