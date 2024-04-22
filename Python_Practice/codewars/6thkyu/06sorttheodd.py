# You will be given an array of numbers. You have to sort the odd numbers in ascending 
# order while leaving the even numbers at their original positions.

# Examples
# [7, 1]  =>  [1, 7]
# [5, 8, 6, 3, 4]  =>  [3, 8, 6, 5, 4]
# [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]  =>  [1, 

# -------------------------------------------------------------------------------------
# -----Solution 1-----Using List Comprehension and sorted-----
def sort_array(arr):
  odds = sorted((x for x in arr if x%2 != 0), reverse=True)
  return [x if x%2==0 else odds.pop() for x in arr]
#   1. Create a variable named odds and set it equal to a list comprehension.
#   2. Iterate over list of numbers in arr.
#   3. If number is odd, add it to list.
#   4. Sort list in descending order.
#   5. Return a list comprehension that iterates over list of numbers in arr.
#   6. If number is even, return number.
#   7. If number is odd, pop last number from odds list and return it.

# -------------------------------------------------------------------------------------
# -----Solution 2-----List Comprehension & Sorted & Append-----
def sort_array(source_array):

    odds = []
    answer = []
    
    for i in source_array:
        if i % 2 > 0:
            odds.append(i)
            answer.append("X")
            
        else:
            answer.append(i)
            
    odds.sort()
    
    for i in odds:
        x = answer.index("X")
        answer[x] = i
    return answer

#   1. Create a variable named odds and set it equal to an empty list.
#   2. Create a variable named answer and set it equal to an empty list.
#   3. Create a for loop to iterate over list of numbers in source_array.
#   4. If number is odd, append it to odds list and append string "X" to answer list.
#   5. If number is even, append number to answer list.
#   6. Sort odds list.
#   7. Create a for loop to iterate over list of numbers in odds.
