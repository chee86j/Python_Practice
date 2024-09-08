# Sum of Pairs

# Given a list of integers and a single sum value, return the first two values 
# (parse from the left please) in order of appearance that add up to form the sum.

# If there are two or more pairs with the required sum, the pair whose second 
# element has the smallest index is the solution.

# sum_pairs([11, 3, 7, 5],         10)
# #              ^--^      3 + 7 = 10
# == [3, 7]

# sum_pairs([4, 3, 2, 3, 4],         6)
# #          ^-----^         4 + 2 = 6, indices: 0, 2 *
# #             ^-----^      3 + 3 = 6, indices: 1, 3
# #                ^-----^   2 + 4 = 6, indices: 2, 4
# #  * the correct answer is the pair whose second value has the smallest index
# == [4, 2]

# sum_pairs([0, 0, -2, 3], 2)
# #  there are no pairs of values that can be added to produce 2.
# == None/nil/undefined (Based on the language)

# sum_pairs([10, 5, 2, 3, 7, 5],         10)
# #              ^-----------^   5 + 5 = 10, indices: 1, 5
# #                    ^--^      3 + 7 = 10, indices: 3, 4 *
# #  * the correct answer is the pair whose second value has the smallest index
# == [3, 7]

# Negative numbers and duplicate numbers can and will appear.

# NOTE: There will also be lists tested of lengths upwards of 10,000,000 elements. 
# Be sure your code doesn't time out.

# -------------------------------------------------------------------------------------
# -----Solution 1----Set for Complements----Easy to Follow----
def sum_pairs(lst, s):
    cache = set()
    for i in lst:
        if s - i in cache:
            return [s - i, i]
        cache.add(i)
#   1. Create a set to store the complements of the numbers in the list w/ respect to the sum
#   2. Iterate through the numbers in the list w/ a for loop
#   3. If the complement of the current number is in the set, return the complement & the current number
#   4. Else, add the current number through the set & continue to the next number
#   5. Return None if no pairs are found

#   This solution uses a set to track the numbers seen so far. For each number in the list, 
#   it checks whether the complement (i.e., s - current_number) exists in the set. If it does,
#   it returns the pair immediately, making sure tthat it returns the first valid pair found from
#   the left. If no pair is found, it adds the current number to the set & continues to the next number. 
#   The time complexity of this solution is O(n) because it iterates through the list of numbers once. 
#   The space complexity is also O(n) in the worst case, where all numbers are unique & no pairs are found. 
#   The space complexity is O(1) in the best case where the first pair found is the correct answer. 
#   This solution is efficient for large lists of numbers because it only requires a single pass through the list.

# -------------------------------------------------------------------------------------
# -----Solution 2----Similar Approach w/different Syntax----
def sum_pairs(nums, sum_value):
    seen = set()
    for num in nums:
        diff = sum_value - num
        if diff in seen:
            return [diff, num]
        seen.add(num)
        
# -------------------------------------------------------------------------------------
# -----Solution 3----Alternative Approach w/Complements----
def sum_pairs(ints, s):
    d = set()
    for n in ints:
        if n in d: return [s - n, n]
        d.add(s - n)
#   1. Create a set to store the complements of the numbers in the list w/ respect to the sum
#   2. Iterate through the numbers in the list w/ a for loop
#   3. If the current number is in the set, return the complement & the current number
#   4. Else, add the complement of the current number through the set & continue to the next number
#   5. Return None if no pairs are found

#   This solution is similar to the previous ones but uses the complement of the current number 
#   (i.e., s - current_number) as the key to check whether the current number is in the set.
#   If the current number is in the set, it means that the complement has been seen before,
#   & the function returns the pair immediately. This solution has the same time & space
#   complexity as the previous one. It is also efficient for large lists of numbers because it
#   only requires a single pass through the list. It is less intuitive than Solution 1 & Solution 2
#   because it uses the complement as the key to check for the presence of the current number in the set.
        
# -------------------------------------------------------------------------------------
# -----Solution 4----JavaScript Solution----
# function sumPairs(lst, s) {
#     const cache = new Set();
#     for (let i of lst) {
#         if (cache.has(s - i)) {
#             return [s - i, i];
#         }
#         cache.add(i);
#     }
#     return undefined;  // Return undefined if no pair is found
# }
#   Similar to the Python solutions, this JavaScript solution uses a set to store the complements of 
#   the numbers in the list with respect to the sum. It iterates through the numbers in the list & 
#   checks whether the complement of the current number is in the set. If it is, it returns the pair
#   immediately. If no pair is found, it returns undefined. This solution has the same time & space
#   complexity as the Python solutions. It is also efficient for large lists of numbers because it only
#   requires a single pass through the list.