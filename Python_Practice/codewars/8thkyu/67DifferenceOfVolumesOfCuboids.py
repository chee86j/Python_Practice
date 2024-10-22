# Description:
    
# In this simple exercise, you will create a program that will take 
# two lists of integers, a and b. Each list will consist of 3 positive 
# integers above 0, representing the dimensions of cuboids a and b. 
# You must find the difference of the cuboids' volumes regardless of 
# which is bigger.

# For example, if the parameters passed are ([2, 2, 3], [5, 4, 1]), 
# the volume of a is 12 and the volume of b is 20. Therefore, the 
# function should return 8.

# Your function will be tested with pre-made examples as well as random 
# ones.

# If you can, try writing it in one line of code.

# -------------------------------------------------------------------------------------
# -----Solution 1-----prod() & abs()-----
from numpy import prod

def find_difference(a, b):
    return abs(prod(a) - prod(b))
#   1.  Import the prod() function from the numpy module.
#   2.  The find_difference function takes two lists, a & b, as input.
#   3.  The prod() function is used to calculate the product of all the elements in the list `a`.
#       All three dimensions are multiplied together to get the volume of the cuboid 
#       represented by list `a`.

#   This solution using the prod() function from the numpy module is a direct & concise,
#   however, it requires importing the numpy library is overkill & increases the complexity
#   & size of the code. It is useful when dealing with large datasets or when the number of
#   elements in the list is very large.

#   The time complexity of this solution is O(n) where n is the number of elements in the list.
#   The space complexity is also O(n) since the prod() function creates a new list to store the
#   product of the elements in the input list.


# -------------------------------------------------------------------------------------
# -----Solution 2-----Multiplying Directly by Index-----
def find_difference(a, b):
	return abs((a[1]*a[2]*a[0])-b[1]*b[2]*b[0])
#   1.  The find_difference function takes two lists, a & b, as input.
#   2.  The volume of the cuboid represented by list `a` is calculated by multiplying the
#       three dimensions together: a[0] * a[1] * a[2].
#   3.  The volume of the cuboid represented by list `b` is calculated in the same way: 
#       b[0] * b[1] * b[2].
#   4.  The absolute difference between the volumes of the two cuboids is calculated by 
#       subtractingb the volume of the cuboid represented by list `b` from the volume of 
#       the cuboid represented by list `a`.
#   5.  The abs() function is used to ensure that the difference is positive.
#   6.  The result is returned.

#   This solution is simple & easy to understand & doesn't need any external libraries. It is
#   straightforwards & readable. It is useful when dealing with small datasets or when the number
#   of elements in the list is small.

#   The time complexity of this solution is O(1) since it only involves simple arithmetic operations.
#   The space complexity is also O(1) since it only uses a few variables to store the volumes of the
#   cuboids.

# -------------------------------------------------------------------------------------
# -----Solution 3-----Multiplying Using Index Access-----
def find_difference(a, b):
	return abs(a[0] * a[1] * a[2] - b[0] * b[1] * b[2])
#   1.  The find_difference function takes two lists, a & b, as input.
#   2.  The volume of the cuboid represented by list `a` is calculated by multiplying the
#       three dimensions together: a[0] * a[1] * a[2].
#   3.  The volume of the cuboid represented by list `b` is calculated in the same way:
#       b[0] * b[1] * b[2].
#   4.  The absolute difference between the volumes of the two cuboids is calculated by
#       subtracting the volume of the cuboid represented by list `b` from the volume of
#       the cuboid represented by list `a`.
#   5.  The abs() function is used to ensure that the difference is positive.
#   6.  The result is returned.

#   This solution is similar to solution 2, but is more organized & easier to read. It is useful
#   when dealing with small datasets or when the number of elements in the list is small.

#   The time complexity of this solution is O(1) since it only involves simple arithmetic operations.
#   The space complexity is also O(1) since it only uses a few variables to store the volumes of the
#   cuboids.

# -------------------------------------------------------------------------------------
# -----Solution 4-----Javascript Solution-----Reduce() & Math.abs() & Arrow Functions-----
# function find_difference(a, b) {
#   return Math.abs(a.reduce((previous, current) => previous * current) - b.reduce((previous, current) => previous * current));
# }
#   1.  The find_difference function takes two lists, a & b, as input.
#   2.  The reduce() method is used to calculate the product of all the elements in the list `a`.
#       The arrow function (previous, current) => previous * current is used to multiply the
#       elements together.
#   3.  The reduce() method is also used to calculate the product of all the elements in the list `b`.
#   4.  The absolute difference between the volumes of the two cuboids is calculated by subtracting
#       the product of the elements in list `b` from the product of the elements in list `a`.
#   5.  The Math.abs() function is used to ensure that the difference is positive.
#   6.  The result is returned.

#   This solution uses the reduce() method to calculate the product of the elements in the input lists.
#   It is concise & uses arrow functions to define the multiplication operation. It is useful when
#   dealing with large datasets or when the number of elements in the list is very large.

#   The time complexity of this solution is O(n) where n is the number of elements in the list.
#   The space complexity is also O(n) since the reduce() method creates a new list to store the product
#   of the elements in the input list.
