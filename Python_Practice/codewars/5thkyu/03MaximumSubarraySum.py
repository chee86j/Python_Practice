# The maximum sum subarray problem consists in finding the 
# maximum sum of a contiguous subsequence in an array or 
# list of integers:

# max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4])
# # should be 6: [4, -1, 2, 1]
# Easy case is when the list is made up of only positive 
# numbers and the maximum sum is the sum of the whole 
# array. If the list is made up of only negative numbers, 
# return 0 instead.

# Empty list is considered to have zero greatest sum. Note 
# that the empty list or array is also a valid sublist/subarray.

# -------------------------------------------------------------------------------------
# -----Solution 1-----Using Kadane's Algorithm-----
def maxSequence(arr):
    max,curr=0,0    # this is the initialization step which sets max & curr to 0
    for x in arr:   
        curr+=x
        if curr<0:curr=0
        if curr>max:max=curr
    return max


#   1.  Initialization: Two variables are initialized: max_sum to keep track of the maximum 
#       sum we have found, & current_sum to calculate sum of the current subarray.
#   2.  Loop: We iterate over the input array, adding each element to current_sum.
#       a.  If current_sum becomes negative, we reset it to 0. This is because we are
#           looking for the maximum sum subarray, & a negative sum will only decrease the
#           maximum sum.
#       b.  If current_sum is greater than max_sum, we update max_sum.
#   3.  Return: We return max_sum only after the loop ends, which will be the maximum sum of
#       a contiguous (meaning elements are adjacent) subarray in the input array.

#   This problem is solved using Joseph Kadane's algorithm, which is an efficient way to find the maximum sum subarray.
#   It finds the maximum subarray in linear time by keeping track of the maximum sum of subarrays ending at each
#   in O(n) time complexity & O(1) space complexity.

# -------------------------------------------------------------------------------------
# -----Solution 2-----Javascript Version-----
# function maxSequence(arr) {
#     let maxSum = 0;
#     let currentSum = 0;

#     for (let x of arr) {
#         currentSum += x;
#         if (currentSum < 0) {
#             currentSum = 0;
#         }
#         if (currentSum > maxSum) {
#             maxSum = currentSum;
#         }
#     }
#     return maxSum;
# }
