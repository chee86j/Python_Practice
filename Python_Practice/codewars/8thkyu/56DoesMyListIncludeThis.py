# Create a method that accepts a list and an item, and returns true 
# if the item belongs to the list, otherwise false.

# -------------------------------------------------------------------------------------
# -----Solution 1----In Operator-----
def include(arr, item):
    return item in arr
#   1.  The () takes two arguments, `arr` & `item`, as input.
#   2.  It uses the `in` operator to check if `item` is present in the `arr` list.
#   3.  If `item` is present in the `arr` list, the () returns True. Otherwise, it returns False.
#   4.  This solution has a time complexity of O(n) because the `in` operator iterates over the elements of the `arr` list
#       to check if `item` is present and a space complexity is O(1) because the () uses a constant amount of extra space.

# -------------------------------------------------------------------------------------
# -----Solution 2----Javascript Solution-----
# function include(arr, item) {
# 	return arr.includes(item);
# }
#   1.  This JS solution is similar to Solution 1. It uses the includes() method to check if `item` is present in the `arr` array.
#   2.  If `item` is present in the `arr` array, the () returns true. Otherwise, it returns false.
#   3.  This solution has a time complexity of O(n) because the includes() method iterates over the elements of the `arr` array to check if
#       `item` is present. The space complexity is O(1) because the () uses a constant amount of extra space. The includes() method provides
#       a simple & concise way to check if an element is present in an array.

