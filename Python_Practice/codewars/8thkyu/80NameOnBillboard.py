# You can print your name on a billboard ad. Find out how much it will cost you. 
# Each character has a default price of £30, but that can be different if you are 
# given 2 parameters instead of 1 (allways 2 for Java).

# You can not use multiplier "*" operator.

# If your name would be Jeong-Ho Aristotelis, ad would cost £600. 
# 20 leters * 30 = 600 (Space counts as a character).

# -------------------------------------------------------------------------------------
# -----Solution 1-----Generator Expression-----
def billboard(name, price=30):
    return sum(price for letter in name)
#   1. A generator expression is used to iterate over the name string by using the for
#      loop to get each letter. `price for letter in name`
#   2. The sum() function is used to sum the price of each letter in the name string.
#      `sum(price for letter in name)`
#   3. The sum of the price of each letter in the name string is returned.
#      `return sum(price for letter in name)`

#   The time complexity of this solution is O(n) where n is the length of the name string 
#   since the generator expression iterates over each character once.
#   The space complexity of this solution is O(1) since the generator expression does not
#   create a list in memory.
#   This is the most effective solution because it leverages built-in functions and
#   generator expressions to calculate the total cost of the billboard.

# -------------------------------------------------------------------------------------
# -----Solution 2-----Verbose For Loop-----Beginner Friendly-----
def billboard(name, price=30):
    count = 0
    for letters in name:
        count += price
    return count
#   1. A variable `count` is initialized to 0 to store the total cost of the billboard.
#      `count = 0`
#   2. A for loop is used to iterate over each letter in the name string.
#      `for letters in name:`
#   3. The price of each letter is added to the `count` variable.
#      `count += price`
#   4. The total cost of the billboard is returned.
#      `return count`

#   The time complexity of this solution is O(n) where n is the length of the name string
#   since the for loop iterates over each character once.
#   The space complexity of this solution is O(1) since only a single variable is used to
#   store the total cost of the billboard.


# -------------------------------------------------------------------------------------
# -----Solution 3-----JavaScript Solution-----
# function billboard(name, price = 30){
# var totalCost = 0;
# for(i=0; i<name.length; i++){
#     totalCost += price;
# } 
# return totalCost;
# }
#   1. A variable `totalCost` is initialized to 0 to store the total cost of the billboard.
#      `var totalCost = 0;`
#   2. A for loop is used to iterate over each letter in the name string.
#      `for(i=0; i<name.length; i++){`
#   3. The price of each letter is added to the `totalCost` variable.
#      `totalCost += price;`
#   4. The total cost of the billboard is returned.
#      `return totalCost;`

#   The time complexity of this solution is O(n) where n is the length of the name string
#   since the for loop iterates over each character once.
#   The space complexity of this solution is O(1) since only a single variable is used to
#   store the total cost of the billboard.
