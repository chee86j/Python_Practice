# Enough is enough!
# Alice and Bob were on a holiday. Both of them took many pictures of 
# the places they've been, and now they want to show Charlie their entire 
# collection. However, Charlie doesn't like these sessions, since the motif 
# usually repeats. He isn't fond of seeing the Eiffel tower 40 times.
# He tells them that he will only sit for the session if they show the 
# same motif at most N times. Luckily, Alice and Bob are able to encode 
# the motif as a number. Can you help them to remove numbers such that 
# their list contains each number only up to N times, without changing 
# the order?

# Task
# Given a list and a number, create a new list that contains each number of 
# list at most N times, without reordering.
# For example if input number is 2, and input list is [1,2,3,1,2,1,2,3], 
# you take [1,2,3,1,2], drop next [1,2] since this would lead to 1 and 2 being 
# in result 3 times, and then take 3, which leads to [1,2,3,1,2,3].
# With list [20,37,20,21] and number 1, result would be [20,37,21].

# -------------------------------------------------------------------------------------
# -----Solution 1-----Count-----
def delete_nth(order,max_e):
    answer = []
    for o in order:
        if answer.count(o) < max_e: answer.append(o)
    return answer
#   1. Create a var named answer and set it equal to an empty list.
#   2. Create a for loop to iterate over each element in order.
#   3. If count of element in answer is less than max_e, append element to answer.
#   4. Return answer.

# -------------------------------------------------------------------------------------
# -----Solution 2-----Dictionary, List Comprehension, & Append-----
def delete_nth(order, max_e):
    d = {}
    res = []
    for item in order:
      n = d.get(item, 0)
      if n < max_e:
        res.append(item)
        d[item] = n+1
    return res
#   1. Create a dictionary named d and set it equal to an empty dictionary.
#   2. Create a var named res and set it equal to an empty list.
#   3. Create a for loop to iterate over each element in order.
#   4. Create a var named n and set it equal to value of element in d.
#   5. If n is less than max_e, append element to res.
#   6. Add 1 to value of element in d.
#   7. Return res.
