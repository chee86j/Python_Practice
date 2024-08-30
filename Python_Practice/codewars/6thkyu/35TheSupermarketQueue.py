# Description:
# There is a queue for the self-checkout tills at the supermarket. 
# Your task is write a function to calculate the total time required 
# for all the customers to check out!

# input
#   -customers: an array of positive integers representing the queue. 
#    Each integer represents a customer, and its value is the amount 
#    of time they require to check out.
#   -n: a positive integer, the number of checkout tills.

# output
# The function should return an integer, the total time required.

# Important
# Please look at the examples and clarifications below, to ensure you 
# understand the task correctly :)

# Examples
# queue_time([5,3,4], 1)
#   should return 12
#   because when n=1, the total time is just the sum of the times

# queue_time([10,2,3,3], 2)
#   should return 10
#   because here n=2 and the 2nd, 3rd, and 4th people in the 
#   queue finish before the 1st person has finished.

# queue_time([2,3,10], 2)
#   should return 12

# Clarifications
#   -There is only ONE queue serving many tills, and
#   -The order of the queue NEVER changes, and
#   -The front person in the queue (i.e. the first element in the array/list) 
#    proceeds to a till as soon as it becomes free.

# N.B. You should assume that all the test input will be valid, as specified above.

# P.S. The situation in this kata can be likened to the more-computer-science-related 
# idea of a thread pool, with relation to running multiple processes at the same 
# time: https://en.wikipedia.org/wiki/Thread_pool

# -------------------------------------------------------------------------------------
# -----Solution 1----List & Indexing-----Efficient-----
def queue_time(customers, n):
    l=[0]*n
    for i in customers:
        l[l.index(min(l))]+=i
    return max(l)
#   1.  The () takes two arguments, `customers` & `n`, as input.
#   2.  It initializes a list, `l`, with `n` elements, each set to 0.
#   3.  Then iterates over each customer in the `customers` list.
#   4.  For each customer, it finds the index of the minimum value in the `l` list 
#       using the index() method.
#   5.  It then adds the time required for the customer to the element at that index 
#       in the `l` list.
#   6.  After processing all customers, it returns the maximum value in the `l` list, 
#       which represents the total time required.

#   This solution initializes an array with `n` zeros represting the time taken for each 
#   till to process a customer. Each customer is then added to the till with the least
#   time accumulated so far. This returns the maximum time from the list of till times
#   & updating it for every customer. It is not the most efficient solution as it uses
#   the index() method to find the minimum value in the list for each customer, which
#   has a time complexity of O(n). 

# -------------------------------------------------------------------------------------
# -----Solution 2----Heapq & Heapreplace-----Most Efficient-----
import heapq

def queue_time(customers, n):
    heap = [0] * n
    for time in customers:
        heapq.heapreplace(heap, heap[0] + time)
    return max(heap)
#   1.  The () takes two arguments, `customers` & `n`, as input.
#   2.  It initializes a heap, `heap`, with `n` elements, each set to 0.
#   3.  Then iterates over each customer in the `customers` list.
#   4.  For each customer, it uses the heapreplace() function from the heapq module to
#       replace the smallest element in the heap with the sum of the smallest element &
#       the time required for the customer.
#   5.  After processing all customers, it returns the maximum value in the `heap`, which
#       represents the total time required.

#   Compared to Solution 1, this solution is more efficient as it uses a heap data structure
#   to keep track of the checkout times for each till. The heapreplace() function allows
#   for efficient replacement of the smallest element in the heap with the sum of the smallest
#   element & the time required for the customer. It has atime complexity of O(n log n)
#   because it iterates over each customer in the `customers` list & performs a log n operation to
#   maintain the heap property. It is faster for large inputs compared to Solution 1.


# -------------------------------------------------------------------------------------
# -----Solution 3----Sorting-----Least Efficient-----
def queue_time(customers, n):
    qn = [0] * n
    for c in customers:
        qn = sorted(qn)
        qn[0] += c
    return max(qn)
#   1.  The () takes two arguments, `customers` & `n`, as input.
#   2.  It initializes a list, `qn`, with `n` elements, each set to 0.
#   3.  Then iterates over each customer in the `customers` list.
#   4.  For each customer, it sorts the `qn` list in ascending order.
#   5.  It then adds the time required for the customer to the first element of the sorted list.
#   6.  After processing all customers, it returns the maximum value in the `qn` list, which 
#       represents the total time required.

#   This solution has a time complexity of O(n^2 log n) because it iterates over each 
#   customer in the `customers` list & performs a log n operation to sort the list. 
#   The space complexity is O(n) because it creates a list of size `n` to store the 
#   checkout times for each till. Compared to Solution 1, this solution is less efficient
#   as it uses the sorted() function to sort the list for each customer, resulting in a
#   higher time complexity. Sorting every iteration is computationally expensive & unnecessary.


# -------------------------------------------------------------------------------------
# -----Solution 4----
# function queueTime(customers, n) {
#   var w = new Array(n).fill(0);
#   for (let t of customers) {
#     let idx = w.indexOf(Math.min(...w));
#     w[idx] += t;
#   }
#   return Math.max(...w);
# }
#   1.  This Javascript solution is similar to Solution 1. It initializes an array, `w`, 
#       with `n` elements, each set to 0.
#   2.  It then iterates over each customer in the `customers` array.
#   3.  For each customer, it finds the index of the minimum value in the `w` array using
#       the indexOf() method.
#   4.  It then adds the time required for the customer to the element at that index in the `w` array.
#   5.  After processing all customers, it returns the maximum value in the `w` array, which represents 
#       the total time required.

#   Similar to Solution 1, this performs a linear search for the minimum value in the array for each customer,
#   which has a time complexity of O(n). The space complexity is O(n) because it creates an array of size `n`
#   to store the checkout times for each till. This solution is concise and straightforward, using simple
#   comparisons to check the conditions. The frequent use of the Math.min() & Math.max() functions makes it
#   can increase the time complexity for large inputs.
