# A string is considered to be in title case if each word in 
# the string is either (a) capitalised (that is, only the first 
# letter of the word is in upper case) or (b) considered to be 
# an exception and put entirely into lower case unless it is 
# the first word, which is always capitalised.

# Write a function that will convert a string into title case, 
# given an optional list of exceptions (minor words). The list 
# of minor words will be given as a string with each word 
# separated by a space. Your function should ignore the case of 
# the minor words string -- it should behave in the same way even 
# if the case of the minor word string is changed.

# Arguments (Haskell)

#     First argument: space-delimited list of minor words that must 
#     always be lowercase except for the first word in the string.
#     Second argument: the original string to be converted.

# Arguments (Other languages)
#     First argument (required): the original string to be converted.
#     Second argument (optional): space-delimited list of minor words 
#     that must always be lowercase except for the first word in the 
#     string. The JavaScript/CoffeeScript tests will pass undefined 
#     when this argument is unused.

# Example

# title_case('a clash of KINGS', 'a an the of') # should return: 'A Clash of Kings'
# title_case('THE WIND IN THE WILLOWS', 'The In') # should return: 'The Wind in the Willows'
# title_case('the quick brown fox') 

# -----------------------------------My Notes-----------------------------------
# This problem is asking to capitalize the 1st letter of each word in a string
# unless the word is in a list of minor words. If the word is in the list of minor
# words, then the word should be lowercase. The 1st word should always be capitalized.


# -------------------------------------------------------------------------------------
# -----Solution 1-----Capitalize & Split & Join & List Comprehension & Conditional-----
def title_case(title, minor_words=''):
    title = title.capitalize().split()
    minor_words = minor_words.lower().split()
    return ' '.join([word if word in minor_words else word.capitalize() for word in title])
# 1. Capitalize 1st letter of 1st word of title
# 2. Split title into a list of words
# 3. Split minor_words into a list of words
# 4. List comprehension to iterate through title list using word as the iterator
# 5. If word is in minor_words list, return word as is
# 6. Else return word capitalized

# -------------------------------------------------------------------------------------
# -----Solution 2-----Similar to Solution 1 but using a for loop instead of list comprehension-----
def title_case(title, minor_words=''):
    title, minor_words = title.lower().split(), minor_words.lower().split()
    for i in range(len(title)):
        if i == 0 or title[i] not in minor_words:
            title[i] = title[i].capitalize()
    return ' '.join(title)
# 1. Split title into a list of words & assign to title
# 2. Split minor_words into a list of words & assign to minor_words
# 3. Iterate through title list using a for loop
# 4. If i is 0 or title[i] is not in minor_words, capitalize title[i]
# 5. Return title list joined into a string

# -------------------------------------------------------------------------------------
# -----Solution 3-----JavaSript Solution-----
# function titleCase(title, minorWords) {
#   var minorWords = typeof minorWords !== "undefined" ? minorWords.toLowerCase().split(' ') : [];
#   return title.toLowerCase().split(' ').map(function(v, i) {
#     if(v != "" && ( (minorWords.indexOf(v) === -1) || i == 0)) {
#       v = v.split('');
#       v[0] = v[0].toUpperCase();
#       v = v.join('');
#     }
#     return v;
#   }).join(' ');
# }

# 1. Store in new var minorWords the lowercase split of minorWords if it is not undefined
# 2. Return the lowercase split of title
# 3. Then map through the split title
# 4. If v is not an empty str and (v is not in minorWords or i is 0)
# 5. Split v into a list of chars
# 6. Capitalize the 1st char of v
# 7. Join v into a string
# 8. Return v