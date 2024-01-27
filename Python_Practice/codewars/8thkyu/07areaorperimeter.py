# You are given the length and width of a 4-sided polygon. The polygon can either be a rectangle or a square.
# If it is a square, return its area. If it is a rectangle, return its perimeter.

# Example(Input1, Input2 --> Output):

# 6, 10 --> 32
# 3, 3 --> 9

# Note: for the purposes of this kata you will assume that it is a square if its length and width are equal, otherwise it is a rectangle.

# -------------------------------------------------------------------------------------
# -----Solution 1-----Ternary Operator-----
def area_or_perimeter(l, w):
    return l * w if l == w else 2 * (l + w)

# -------------------------------------------------------------------------------------
# -----Solution 2-----If Else-----
def area_or_perimeter(l , w):
    if l == w:
        tot = l * w
    else:
        tot = l * 2 + w * 2
    return tot
    
# -------------------------------------------------------------------------------------
# -----Solution 3-----Ternary Operator citing the condition first-----
def area_or_perimeter(l , w):
    
    if l == w: # test for a square
        return (l*w)
    else:       
        return ((2*l)+(2*w))