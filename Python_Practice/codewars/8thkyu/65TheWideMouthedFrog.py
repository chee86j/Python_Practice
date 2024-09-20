# The wide-mouth frog is particularly interested in the eating 
# habits of other creatures.

# He just can't stop asking the creatures he encounters what 
# they like to eat. But, then he meets the alligator who just 
# LOVES to eat wide-mouthed frogs!

# When he meets the alligator, it then makes a tiny mouth.

# Your goal in this kata is to create complete the mouth_size 
# method this method takes one argument animal which corresponds 
# to the animal encountered by the frog. If this one is an alligator 
# (case-insensitive) return small otherwise return wide.

# -------------------------------------------------------------------------------------
# -----Solution 1-----Ternary Operator using If/Else-----
def mouth_size(animal): 
    return 'small' if animal.lower() == 'alligator' else 'wide'
#   1.  This () function converts the animal to lowercase and checks if it is equal to 'alligator'
#       `animal.lower() == 'alligator'`
#   2.  If the animal is an alligator, it returns 'small'
#       `return 'small'`
#   3.  Otherwise, it returns 'wide'
#       `else 'wide'`
#   This solution is the most efficient and easy to understand. It has a time complexity of O(1)
#   because it only checks if the animal is an alligator. The space complexity is O(1) because it
#   only returns a string.

# -------------------------------------------------------------------------------------
# -----Solution 2-----Refactored Solution 1-----
def mouth_size(animal): 
  return 'wide' if animal.lower() != 'alligator' else 'small'
#   1.  This () function converts the animal to lowercase and checks if it is not equal to 'alligator'
#       `animal.lower() != 'alligator'`
#   2.  If the animal is not an alligator, it returns 'wide'
#       `return 'wide'`
#   3.  Otherwise, it returns 'small'
#       `else 'small'`
#   This solution is the most efficient and easy to understand. It has a time complexity of O(1)
#   because it only checks if the animal is an alligator. The space complexity is O(1) because it
#   only returns a string.

# -------------------------------------------------------------------------------------
# -----Solution 3-----Multiple Steps-----
def mouth_size(animal): 
  animal1 = animal.lower()
  if animal1 == 'alligator':
      return 'small'
  else:
      return 'wide'
#   1.  This () function converts the animal to lowercase
#       `animal1 = animal.lower()`
#   2.  It checks if the animal is an alligator
#       `if animal1 == 'alligator':`
#   3.  If the animal is an alligator, it returns 'small'
#       `return 'small'`
#   4.  Otherwise, it returns 'wide'
#       `else 'wide'`
#   This solution is less efficient and harder to read. In terms of readability, it is harder to
#   understand. The time complexity is O(1) because it only checks if the animal is an alligator.
#   The space complexity is O(1) because it only returns a string.
  
# -------------------------------------------------------------------------------------
# -----Solution 4-----Javascript Solution-----
# function mouthSize(animal) {
#   return animal.toLowerCase() == 'alligator' ? 'small' : 'wide';
# }
#   1.  This () function converts the animal to lowercase and checks if it is equal to 'alligator'
#       `animal.toLowerCase() == 'alligator'`
#   2.  If the animal is an alligator, it returns 'small'
#       `return 'small'`
#   3.  Otherwise, it returns 'wide'
#       `else 'wide'`
#   This is the same as the first solution, but written in JavaScript. It is the most efficient
#   and easy to understand. It has a time complexity of O(1) because it only checks if the animal
#   is an alligator. The space complexity is O(1) because it only returns a string.
