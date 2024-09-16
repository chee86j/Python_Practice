# A stream of data is received and needs to be reversed.

# Each segment is 8 bits long, meaning the order of these 
# segments needs to be reversed, for example:

# 11111111  00000000  00001111  10101010
#  (byte1)   (byte2)   (byte3)   (byte4)

# should become:

# 10101010  00001111  00000000  11111111
#  (byte4)   (byte3)   (byte2)   (byte1)

# The total number of bits will always be a multiple of 8.

# The data is given in an array as such:

# [1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,0,1,0,1,0,1,0]

# Note: In the C and NASM languages you are given the third 
# parameter which is the number of segment blocks.

# -------------------------------------------------------------------------------------
# -----Solution 1-----For Loop & List Slicing & Extend-----
def data_reverse(data):
  res = []
  
  for i in range(len(data)-8, -1, -8):
    res.extend(data[i:i+8])
  
  return res
#   1. Create an empty list `res` to store the reversed data
#   2. Iterate over the data in reverse order with a step of 8 using the range function
#      `for i in range(len(data)-8, -1, -8):` which starts from the last segment of 8 bits
#      and goes backwards by 8 bits
#   3. Extend the `res` list with the current segment of 8 bits using list slicing
#      `res.extend(data[i:i+8])`
#   4. Return the reversed data `res`

#   This solution has a time complexity of O(n) where n is the number of bits in the data
#   since it iterates over the data once and a space complexity of O(n) since it creates a new
#   list to store the reversed data. This solution is optimal for reversing the data in a
#   stream of bits. It is clear and concise, using list slicing and the extend method to
#   reverse the data efficiently.

# -------------------------------------------------------------------------------------
# -----Solution 2-----List Comprehension for Single-Line Reversal-----
def data_reverse(data):
    return [b for a in range(len(data) - 8, -1, -8) for b in data[a:a + 8]]
#   1. Use a list comprehension to iterate over the data in reverse order with a step of 8
#      and extract the segments of 8 bits
#   2. Return the reversed data as a list

#   This solution has a time complexity of O(n) where n is the number of bits in the data
#   since it iterates over the data once and a space complexity of O(n) since it creates a new
#   list to store the reversed data. This solution is concise and uses list comprehension to
#   achieve the same result as the previous solution. It is a single-line solution that is
#   easy to read and understand, however, it may be less readable for beginners.


# -------------------------------------------------------------------------------------
# -----Solution 3-----Modular Approach w/ Blockify & Unblockify Functions-----
def blockify(data):
    result = []
    for i in range(0, len(data), 8):
        result.append(data[i:i+8])
    return result

def unblockify(blocks):
    return [bit for block in blocks for bit in block]

def data_reverse(data):
    return unblockify(blockify(data)[::-1])
#   1. Define a function `blockify` that takes a list of bits and groups them into blocks of 8 bits
#   2. Define a function `unblockify` that takes a list of blocks and flattens them into a single list
#   3. Use the `blockify` function to group the data into blocks of 8 bits, reverse the order of the blocks,
#      and then use the `unblockify` function to flatten the reversed blocks into a single list
#   4. Return the reversed data

#   This solution has a time complexity of O(n) where n is the number of bits in the data since it
#   processes the data twice (once for blockifying and once for unblockifying) and a space complexity
#   of O(n) since it creates new lists to store the blocks and the reversed data. This approach is
#   modular and separates the logic into smaller functions, making it easier to understand and maintain.
#   It's easier to manage and modify but at a slight cost to performance due to function call overhead.

# -------------------------------------------------------------------------------------
# -----Solution 4-----Javascript Solution-----
# const dataReverse = data => {
#   const bytes = [];
#   for (let i = 0; i < data.length; i += 8) {
#     bytes.unshift(...data.slice(i, i + 8));
#   }
#   return bytes;
# };

#   This is a JavaScript solution that reverses the data in segments of 8 bits. It uses a for loop
#   to iterate over the data and slice it into segments of 8 bits. The segments are then unshifted
#   into a new array to reverse their order. The time complexity of this solution is O(n) where n
#   is the number of bits in the data since it iterates over the data once and the space complexity
#   is O(n) since it creates a new array to store the reversed data. This solution is similar to the
#   first Python solution but written in JavaScript. It is concise and efficient for reversing the
#   data in segments of 8 bits.

#   The Python solutions provided above are efficient and effective for reversing the data in segments
#   of 8 bits. They use different approaches such as list slicing, list comprehension, and modular
#   functions to achieve the desired result. Solution 3 offers a modular approach that separates the
#   logic into smaller functions, making it easier to understand and maintain. Solution 2 provides a
#   concise single-line solution using list comprehension, while Solution 1 is a straightforward
#   implementation using a for loop and list slicing. All solutions are optimal for reversing the data
#   in a stream of bits and demonstrate different coding styles and techniques.