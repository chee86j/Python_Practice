# Two red beads are placed between every two blue beads. There are N blue beads. 
# After looking at the arrangement below work out the number of red beads.

# @ @@ @ @@ @ @@ @ @@ @ @@ @

# Implement count_red_beads(n) (in PHP count_red_beads($n); in Java, Javascript, 
# TypeScript, C, C++ countRedBeads(n)) so that it returns the number of red beads.
# If there are less than 2 blue beads return 0.

# -------------------------------------------------------------------------------------
# -----Solution 1-----Simple Arithmetic Solution-----
def count_red_beads(nb):
    return max(0, 2 * (nb - 1) )
#   1. We begin by checking if the number of blue beads is less than 2. If it is, we return 0.
#   2. If the number of blue beads is greater than or equal to 2, we calculate the number of 
#      red beads using the formula 2 * (nb - 1).
#   3. Then return the result of the calculation.

#   The time complexity of this solution is O(1) since the number of operations does not 
#   depend on the size of the input. The space complexity is also O(1) since we are using
#   a constant amount of space to store the result. This solution is efficient and will work
#   for any valid input because of its simple use of arithmetic operations.

# -------------------------------------------------------------------------------------
# -----Solution 2-----Using Ternary Operator-----
def count_red_beads(n_blue):
    return (n_blue - 1) * 2 if n_blue >= 2 else 0
#   1. We use a ternary operator to check if the number of blue beads is greater than or equal to 2.
#   2. If it is, we calculate the number of red beads using the formula (n_blue - 1) * 2.
#   3. If the number of blue beads is less than 2, we return 0.

#   This solution has a time complexity of O(1) and a space complexity of O(1), making it efficient
#   for any valid input. The use of the ternary operator makes the code concise and easy to read.
#   This solution is a good choice for solving the problem in a single line of code, but
#   it may be less readable for beginners compared to the first solution.

# -------------------------------------------------------------------------------------
# -----Solution 3-----Using Conditional Statement-----
def count_red_beads(n):
    return 2*(n - 1) if n > 1 else 0
#   This is a variation of the first solution that uses a conditional statement to check if the number
#   of blue beads is greater than 1. If it is, we calculate the number of red beads using the formula 2 * (n - 1).
#   If the number of blue beads is less than or equal to 1, we return 0.

#   The time complexity of this solution is O(1) and the space complexity is also O(1). This solution is
#   efficient and will work for any valid input. The use of a conditional statement makes the code easy to
#   understand and is suitable for beginners who may find the ternary operator less intuitive.

# -------------------------------------------------------------------------------------
# -----Solution 4-----JavaScript Solution-----
# function countRedBeads(n) {
#     return n > 1 ? 2 * (n - 1) : 0;
# }
#   This JavaScript solution is similar to the third Python solution, using a conditional statement to
#   check if the number of blue beads is greater than 1. If it is, the function calculates the number of
#   red beads using the formula 2 * (n - 1). If the number of blue beads is less than or equal to 1, the
#   function returns 0. This solution has a time complexity of O(1) and a space complexity of O(1), making
#   it efficient for any valid input. The use of a conditional statement makes the code easy to understand
#   and is suitable for beginners who may find the ternary operator less intuitive.
