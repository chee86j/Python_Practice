# DESCRIPTION:
# Complete the function that accepts a string parameter, and reverses each word in the string. All spaces in the string should be retained.

# Examples
# "This is an example!" ==> "sihT si na !elpmaxe"
# "double  spaces"      ==> "elbuod  secaps"

# -------------------------------------------------------------------------------------
# -----Solution 1-----Loops & Join & List Comprehension-----
def reverse_words(str):
    return ' '.join(word[::-1] for word in str.split(' '))
    # starting from the innermost part of the code we have:
    #   str.split(' ') = ['Fast', 'Cars']
    # next we have the list comprehension:
    #   for each word in str.split(' ') we reverse the word
    # word[::-1] reverses the word starting from the last letter to the first
    # finally we join the reversed words with a space in between
    #   ' '.join(word[::-1] for word in str.split(' ')) = 'tsaF sraC'

# -------------------------------------------------------------------------------------
# -----Solution 2-----Loops & Append-----
def reverse_words(str):
  newStr = []
  
  for i in str.split(' '):
      newStr.append(i[::-1])
      
  return ' '.join(newStr)
  # Example of the code above with str = "Fast Cars"
  # newStr = []
  # loop through each word in str.split(' ') = ['Fast', 'Cars']
  # finally we append the reversed words to newStr
  #  newStr.append(i[::-1]) = ['tsaF', 'sraC']

# -------------------------------------------------------------------------------------
# -----Solution 3-----Loops & Concatenation-----
def reverse_words(text):
    words = text.split(' ')
    result = ''
    
    for word in words:
        result += word[::-1] + ' '
    return result [:-1]
    # Example of the code above with str = "Fast Cars"
    # words = ['Fast', 'Cars']
    # result = ''
    # for word in words:
    #     result += word[::-1] + ' '
    # result = 'tsaF sraC'
    # return result [:-1] = 'tsaF sraC'




