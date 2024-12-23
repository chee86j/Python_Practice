# A bookseller has lots of books classified in 26 categories labeled A, B, C, ..., Z. 
# Each book has a code of at least 3 characters. The 1st character of a code is a 
# capital letter which defines the book category.

# In the bookseller's stocklist each code is followed by a space and by a positive integer, 
# which indicates the quantity of books of this code in stock.

# -----TASK-----

# You will receive the bookseller's stocklist and a list of categories. Your task is to find 
# the total number of books in the bookseller's stocklist, with the category codes in the list 
# of categories. Note: the codes are in the same order in both lists.

# Return the result as a string described in the example below, or as a list of pairs (Haskell/Clojure/Racket/Prolog).

# If any of the input lists is empty, return an empty string, or an empty array/list (Clojure/Racket/Prolog).

# -----Example-----

# # the bookseller's stocklist:
# "ABART 20", "CDXEF 50", "BKWRK 25", "BTSQZ 89", "DRTYM 60"

# # list of categories: 
# "A", "B", "C", "W"

# # result:
# "(A : 20) - (B : 114) - (C : 50) - (W : 0)"


# Explanation:
# --category A: 20 books (ABART)
# --category B: 114 books = 25 (BKWRK) + 89 (BTSQZ)
# --category C: 50 books (CDXEF)
# --category W: 0 books

# -------------------------------------------------------------------------------------
# Understanding the Problem

# Given:
    # A stocklist of books with codes and quantities.
    # A list of categories.
    
# You need to:
    # Calculate the total quantity of books for each category in the categories list.
    # Return the result in the format:
            # "(Category : Total) - (Category : Total) ..."

# -------------------------------------------------------------------------------------
# -----Solution 1-----Using collections.defaultdict-----
from collections import defaultdict

def stock_list(stocklist, categories):
    if not stocklist or not categories:
        return ""

    category_totals = defaultdict(int)
    for item in stocklist:
        code, quantity = item.split()
        category = code[0]
        category_totals[category] += int(quantity)

    return " - ".join(f"({cat} : {category_totals[cat]})" for cat in categories)
#   1. Stary by importing defaultdict from collections module.
#   2. Check if either stocklist or categories is empty, return an empty str.
#   3. Create an empty defaultdict called category_totals.
#   4. Loop through each item in the stocklist & split the item into code & quantity.
#   5. Get the category by taking the first character of the code.
#   6. Add the quantity to the category_totals dictionary.
#   7. Return the result in the format "(Category : Total) - (Category : Total) ..."

#   The time complexity is O(n + m) where n is the length of the stocklist & m is the 
#   length of the categories list.
#   The space complexity is O(c) where c is the number of distinct categories in the stocklist.

#   This is the most efficient solution because it uses a defaultdict to store the total 
#   quantities for each category. This allows you to avoid checking if a category is already
#   in the dictionary before adding the quantity. It also uses a generator expression to
#   create the final result str, which is more efficient than using a list comprehension
#   because it doesn't create an intermediate list.

# -------------------------------------------------------------------------------------
# -----Solution 2-----Using Dictionary Comprehension-----
def stock_list(stocklist, categories):
    if not stocklist or not categories:
        return ""

    category_totals = {cat: 0 for cat in categories}
    for item in stocklist:
        code, quantity = item.split()
        if code[0] in category_totals:
            category_totals[code[0]] += int(quantity)

    return " - ".join(f"({cat} : {category_totals[cat]})" for cat in categories)
#   1. Check if either stocklist or categories is empty, return an empty str.
#   2. Create a dictionary comprehension called category_totals with the categories as keys & 0 as values.
#   3. Loop through each item in the stocklist & split the item into code & quantity.
#   4. Check if the first character of the code is in the category_totals dictionary.
#   5. Add the quantity to the category_totals dictionary.
#   6. Return the result in the format "(Category : Total) - (Category : Total) ..."

#   The time complexity is O(n + m) where n is the length of the stocklist & m is the
#   length of the categories list.
#   The space complexity is O(c) where c is the number of distinct categories in the stocklist.

#   This solution is similar to the previous one, but it uses a dictionary comprehension to 
#   create the category_totals dictionary. This is a more concise way to create the dictionary
#   than using a loop. The rest of the solution is the same as the previous one. This solution is
#   is just as efficient as the previous one.

# -------------------------------------------------------------------------------------
# -----Solution 3-----Using Sum with List Comprehension-----
def stock_list(stocklist, categories):
    if not stocklist or not categories:
        return ""

    return " - ".join(f"({cat} : {sum(int(item.split()[1]) for item in stocklist if item[0] == cat)})" for cat in categories)
#   1. Check if either stocklist or categories is empty, return an empty str.
#   2. Use a list comprehension to create the result str for each category.
#   3. For each category, sum the quantities of all items in the stocklist that start with that category.
#      'item.split()[1]' gets the quantity of the item, & 'item[0]' gets the first character of the code.
#      'if item[0] == cat' filters the items by category. 'int()' converts the quantity to an integer.
#      'sum()' adds up all the quantities for that category. 'f' is used to format the result str.
#   4. Return the result in the format "(Category : Total) - (Category : Total) ..."

#   The time complexity is O(n * m) where n is the length of the stocklist & m is the
#   length of the categories list. This is because for each category, you need to sum the
#   quantities of all items in the stocklist that start with that category.
#   The space complexity is O(1) because you are not using any additional space to store
#   the category totals.

#   This solution is less efficient than the previous ones because it uses a list comprehension
#   with a sum function to calculate the total quantity for each category. This requires iterating
#   over the stocklist multiple times for each category, which can be slow for large datasets.

# -------------------------------------------------------------------------------------
# -----Solution 4-----JavaScript Solution-----Using forEach & map-----
# function stockList(listOfArt, listOfCat) {
#   var qs = {};
#   if (!listOfArt.length) return '';

#   listOfArt.forEach(function(art) {
#     var cat = art[0];
#     qs[cat] = (qs[cat] | 0) + +art.split(' ')[1];
#   });

#   return listOfCat.map(function(c) {
#     return '(' + c + ' : ' + (qs[c] | 0) + ')';  
#   }).join(' - ');  
# }
#   1. Create an empty object called 'qs' to store the quantities for each category.
#   2. Check if the listOfArt is empty, return an empty str.
#   3. Loop through each item in the listOfArt using forEach.
#   4. Get the category by taking the first character of the item.
#   5. Add the quantity to the 'qs' object using the category as the key.
#   6. Use map to create the result str for each category in the listOfCat.
#   7. Return the result in the format "(Category : Total) - (Category : Total) ..."

#   This solution is similar to the first two Python solutions, but it uses JavaScript syntax
#   to achieve the same result. It uses forEach to loop through the listOfArt & map to create
#   the result str for each category in the listOfCat. The rest of the solution is the same
#   as the Python solutions.

