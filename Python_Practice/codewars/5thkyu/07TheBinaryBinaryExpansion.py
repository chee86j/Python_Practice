# Normally, we decompose a number into binary digits by assigning 
# it with powers of 2, with a coefficient of 0 or 1 for each term:

# 25 = 1*16 + 1*8 + 0*4 + 0*2 + 1*1

# The choice of 0 and 1 is... not very binary. We shall perform the 
# true binary expansion by expanding with powers of 2, but with a 
# coefficient of 1 or -1 instead:

# 25 = 1*16 + 1*8 + 1*4 - 1*2 - 1*1

# Now this looks binary.


# Given any positive number n, expand it using the true binary 
# expansion, and return the result as an array, from the most 
# significant digit to the least significant digit.

# true_binary(25) == [1,1,1,-1,-1]

# It should be trivial (the proofs are left as an exercise to the 
#                       reader) to see that:

#     Every odd number has infinitely many true binary expansions
#     Every even number has no true binary expansions

# Hence, n will always be an odd number, and you should return the 
# least true binary expansion for any n.

# Also, note that n can be very, very large, so your code should be 
# very efficient.

# -------------------------------------------------------------------------------------
# -----Solution 1-----List Comprehension & String Slicing & bin & Iteration & If Else-----
def true_binary(n):
    return [-1 if x == '0' else 1 for x in bin(n)[1:-1]]
#  1. Convert the number to binary and slice off the first and last characters
#  2. Iterate over the binary number
#  3. If the digit is 0, append -1 to the list
#  4. If the digit is 1, append 1 to the list
#  5. Return the list

#  This solution is efficient because it only iterates over the binary number once
#  and appends to the list based on the value of the digit

# -------------------------------------------------------------------------------------
# --------------------WHY THIS SOLUTION IS WORKS---------------------------------------
#  'bin(n)[1:-1]' straightforwardly maps the binary representation of n directly into +1 and -1,
#  reflecting each bit's status (1 or 0) accurately. It literally translates each bit of the binary 
#  representation into either 1 or -1, which is a more direct and error-free method of achieving 
#  the "true binary" expansion you're seeking.

#  This does not modify nn or attempt to predict the effects of higher or lower bits. It simply assesses 
#  each bit in its current state, making it more reliable for directly translating binary digits 
#  into the desired format.
# -------------------------------------------------------------------------------------

#  Using example 25:
#  1. bin(25) => '0b11001'
#  2. '0b11001'[1:-1] => '1001'
#  3. [-1 if x == '0' else 1 for x in '1001'] => [1, 1, 1, -1]

# -------------------------------------------------------------------------------------
# -----Solution 2-----Bin & List Comprehension & String Slicing & Ternary Operator & If Else-----
    temp=bin(n)[2:]
    return [1 if i=="1" else -1 for i in temp[-1]+temp[:-1]]
#  1. Convert the number to binary, remove the '0b' prefix.
#  2. Reverse the binary digits except for the most significant bit by appending 
#     the least significant bit to the front and then taking the rest from the end to the front.
#  3. Iterate over the adjusted binary string.
#  4. Append +1 if the character is '1', -1 if '0'.
#  5. The list creation follows the true binary expansion with custom adjustments.

#  Using example 25:
#  1. bin(25) => '0b11001'
#  2. '0b11001'[2:] => '11001', temp[-1] + temp[:-1] => '11100'
#  3. [1 if i == "1" else -1 for i in '11100'] => [1, 1, 1, -1, -1]

# -------------------------------------------------------------------------------------
# -----Solution 3-----Ternary Operator & String Slicing & List Comprehension & If Else-----
def true_binary(n):
    return  [1 if d == "1" else -1 for d in (f"1{n>>1:b}" if n > 1 else "1")]
#  1. Use bit manipulation to right-shift the number by 1, then convert to binary.
#  2. Force prepend '1' to handle most significant bit manually, ensuring correct length and significance.
#  3. Iterate over the string, converting '1' to 1 and '0' to -1 in the list.
#  4. Handles all digits by adjusting n and ensuring that the first digit is correctly interpreted as +1.

#  Using example 25:
#  1. n >> 1 => 12, bin(12) => '0b1100'
#  2. '1' + '1100' => '11100'
#  3. [1 if d == "1" else -1 for d in '11100'] => [1, 1, 1, -1, -1]

# -------------------------------------------------------------------------------------
# -----Solution 4-----Bin & List Comprehension & String Slicing & Ternary Operator & If Else-----
def true_binary(n):
    if n==1:return [1]
    s=bin(n)[-1]+bin(n>>1)[2:]
    return [-1 if i=='0' else 1 for i in s]
#  1. Handle the special case where n is exactly 1.
#  2. Perform a right shift on n, then extract all bits except the most significant bit, 
#     prepend the least significant bit of n to handle the final list order directly.
#  3. Iterate over the adjusted binary string, converting '0' to -1 and '1' to +1.
#  4. This construction ensures correct representation with minimal list operations.

#  Using example 25:
#  1. bin(25)[-1] + bin(25 >> 1)[2:] => '1' + '1100' => '11100'
#  2. [-1 if i == '0' else 1 for i in '11100'] => [1, 1, 1, -1, -1]