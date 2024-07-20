# Find the total sum of internal angles (in degrees) 
# in an n-sided simple polygon. N will be greater than 2.

# -------------------------------------------------------------------------------------
# -----Solution 1-----
def angle(n):
    return (n-2) * 180

# 1.  Based on the requirements we know that the sum of the interior angles in a 
#     triangle is 180 degrees.
# 2.  If we take any n-sided polygon (n > 2) and draw diagonals from one vertex to 
#     all other vertices, we will have n-2 triangles.
# 3.  The sum of the interior angles of the polygon will be the sum of the interior
#     angles of all the triangles.
# 4.  The sum of the interior angles of a polygon with n sides is (n-2) * 180.