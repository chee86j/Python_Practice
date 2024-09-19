# Your task, is to create N×N multiplication table, of size provided in parameter.

# For example, when given size is 3:

# 1 2 3
# 2 4 6
# 3 6 9
# For the given example, the return value should be:

# [[1,2,3],[2,4,6],[3,6,9]]

# -------------------------------------------------------------------------------------
# -----Solution 1-----One Liner - List Comprehension & Nested Loop-----
def multiplicationTable(size):
    return [[j*i for j in range(1, size+1)] for i in range(1, size+1)]
#   1.  The list comprehension iterates through the range of 1 to size+1 for the inner list
#       `for j in range(1, size+1)`
#   2.  Then it iterates through the range of 1 to size+1 for the outer list
#       `for i in range(1, size+1)`
#   3.  The list comprehension multiplies the inner list by the outer list
#       `j*i`
#   4.  The list comprehension returns the multiplication table
#       `return [[j*i for j in range(1, size+1)] for i in range(1, size+1)]`

#   This solution is efficient & easy to understand. In terms of readability, it is easy 
#   to understand. The time complexity is O(n^2) because of the nested loop and the space
#   complexity is O(n^2) because of the list comprehension.

# -------------------------------------------------------------------------------------
# -----Solution 2-----For Loop & Nested Loop-----Better for Beginners-----
# def multiplication_table(size):
#     columns = []
#     for i in range(1,size+1):
#         rows = []
#         for j in range(1,size+1):
#             rows.append(i*j)
#         columns.append(rows)
        
#     return columns

#       Compared to the previous solution, this solution is less efficient and harder to read.
#   1.  Start by creating an empty list called columns
#       `columns = []`
#   2.  Tjen iterate through the range of 1 to size+1 for the outer loop
#       `for i in range(1,size+1):`
#       a.  Create an empty list called rows
#           `rows = []`
#       b.  Then iterate through the range of 1 to size+1 for the inner loop
#           `for j in range(1,size+1):`
#           i.  Append the product of i and j to the rows list
#               `rows.append(i*j)`
#       c.  Append the rows list to the columns list
#           `columns.append(rows)`
#   3.  Return the columns list
#       `return columns`

#   This solution is less efficient and harder to read. In terms of readability, it is harder
#   to understand. The time complexity is O(n^2) because of the nested loop and the space
#   complexity is O(n^2) because of the list comprehension. 

# -------------------------------------------------------------------------------------
# -----Solution 3-----Javascript Solution-----
# multiplicationTable = function(size) {
#   var result = [];

#   for (var i = 0; i < size; i++) {
#     result[i] = [];
#     for(var j = 0; j < size; j++) {
#       result[i][j] = (i + 1) * (j + 1);
#     }
#   }
  
#   return result
# }

#   This is the same as the second solution, but written in JavaScript. It is less efficient
#   and harder to read. The time complexity is O(n^2) because of the nested loop and the space
#   complexity is O(n^2) because of the list comprehension.