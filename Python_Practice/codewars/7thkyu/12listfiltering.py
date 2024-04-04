# DESCRIPTION:
# In this kata you will create a function that takes a list of non-negative integers 
# and strings and returns a new list w/ strings filtered out.

# Example
# filter_list([1,2,'a','b']) == [1,2]
# filter_list([1,'a','b',0,15]) == [1,0,15]
# filter_list([1,2,'aasf','1','123',123]) == [1,2,123]

# -------------------------------------------------------------------------------------
# -----Solution 1-----List Comprehension-----
def filter_list(l):
    # 'return a new list w/ strings filtered out'
  return [i for i in l if not isinstance(i, str)]

# 1. 'for i in l' - iterate through list
# 2. 'if not isinstance(i, str)' - check if element is not a string

#       isinstance a function that returns True if specified object 
#       is of specified type, otherwise False

# 3. 'return' - return new list w/ strings filtered out


# -------------------------------------------------------------------------------------
# -----Solution 2-----List Comprehension w/ 'type'-----
def filter_list(l):
  return [x for x in l if type(x) is not str]

# 1. similar to solution 1 but using 'type' instead of 'isinstance'
# 2. list comprehension to iterate through list and check if 
#    element is not a string using 'type(x) is not str'
# 3. if type of 'x' is not a string, return new list


# -------------------------------------------------------------------------------------
# -----Solution 3-----For Loop-----
def filter_list(l):
    new_list =[]
    for x in l:
        if type(x) != str:
            new_list.append(x)
    return new_list

# 1. 'new_list =[]' - create an empty list to store new list
# 2. 'for x in l' - iterate through list
# 3. 'if type(x) != str' - check if element is not a string
# 4. 'new_list.append(x)' - add element to new list
# 5. 'return new_list' - return new list w/ strings filtered out
