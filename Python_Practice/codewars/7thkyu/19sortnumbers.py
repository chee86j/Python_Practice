# Finish the solution so that it sorts the passed in array 
# of numbers. If the function passes in an empty array or 
# null/nil value then it should return an empty array.

# For example:

# solution([1,2,3,10,5])    # should return [1,2,3,5,10]
# solution(None)    # should return []

# -------------------------------------------------------------------------------------
# -----Solution 1-----Conditional & Sort-----
def solution(nums):
    return sorted(nums) if nums else []
#   1. Check if nums is truthy (not null or not empty)
#   2. If nums is truthy, return sorted nums
#   3. If nums is falsy (null or empty), return an empty list

# -------------------------------------------------------------------------------------
# -----Solution 2-----Sort & Or-----
def solution(nums):
    return sorted(nums or [])
#   1. Return sorted nums if nums is truthy
#   2. Return sorted empty list if nums is falsy
#   3. sorted in python will return an empty list if the input is an empty list