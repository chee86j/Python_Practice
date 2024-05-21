# DESCRIPTION:

# Task
# Given a sequence of integers, check whether it is possible to 
# obtain a strictly increasing sequence by erasing no more than 
# one element from it.

# Example
# For sequence = [1, 3, 2, 1], the output should be false;

# For sequence = [1, 3, 2], the output should be true.

# Input/Output
# [input] integer array sequence

# Constraints: 2 ≤ sequence.length ≤ 1000, -10000 ≤ sequence[i] ≤ 10000.

# [output] a boolean value

# true if it is possible, false otherwise.

# -------------------------------------------------------------------------------------
# -----Solution 1-----for loop & enumerate & if else-----
def almost_increasing_sequence(sequence):
    save, first = -float('inf'), True
    for i,x in enumerate(sequence):
        if x > save: save = x
        elif first:
            if i == 1 or x > sequence[i-2]: save = x
            first = False
        else: return False
    return True
#   1.  Initialize save to negative infinity and first to True
#   2.  Loop through the sequence using enumerate
#       Enumerate is used to get the index and the value of the sequence
#   3.  If x is greater than save, set save to x
#   4.  Else if first is True
#   5.  If i is 1 or x is greater than the element before the previous element
#       set save to x
#   6.  Set first to False
#   7.  Else return False


# -------------------------------------------------------------------------------------
# -----Solution 2-----Javascript Solution-----
# function almostIncreasingSequence(seq) {
#   seq=seq.slice()
#   for(var i=0;i<seq.length-1;i++) {
#     if(seq[i]>=seq[i+1]&&i<seq.length-2){
#       seq.splice(i,1)
#       return seq.every((x,j)=>j===seq.length-1||x<seq[j+1])
#     }
#   }
#   return true
# }

#   1.  Create a copy of the sequence
#   2.  Loop through the sequence
#   3.  If the current element is greater than or equal to the next element
#       and the index is less than the length of the sequence minus 2
#   4.  Remove the current element from the sequence using splice, which
#       modifies the original array and returns the removed elements
#   5.  Return true if every element in the sequence is less than the next element
#       or the index is the length of the sequence minus 1
#   6.  Return true if the loop completes