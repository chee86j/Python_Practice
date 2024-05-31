# Your task is to sort a given string. Each word in the string 
# will contain a single number. This number is the position the 
# word should have in the result.

# Note: Numbers can be from 1 to 9. So 1 will be the first word (not 0).

# If the input string is empty, return an empty string. The words in the 
# input String will only contain valid consecutive numbers.

# Examples
# "is2 Thi1s T4est 3a"  -->  "Thi1s is2 3a T4est"
# "4of Fo1r pe6ople g3ood th5e the2"  -->  "Fo1r the2 g3ood 4of th5e pe6ople"
# ""  -->  ""

# -------------------------------------------------------------------------------------
# -----Solution 1-----Join & Sorted & Split & Lambda-----
def order(sentence):
    return " ".join(sorted(sentence.split(), key=lambda x: sorted(x)))
#   1.  Split sentence into a list of words using split method
#   2.  Sort list of words using sorted method
#   3.  Sort words based on sorted order of characters in word
#   4.  Join sorted list of words into a str using join method
#   5.  Return sorted str

# -------------------------------------------------------------------------------------
# -----Solution 2-----If Statement & Split & Append & Join-----
def order(sentence):
    if not sentence:
        return ""
    result = []
    
    split_up = sentence.split()
    
    for i in range(1, 10):
        for item in split_up:
            if str(i) in item:
                result.append(item)
                
    return " ".join(result)
#   1.  Check if sentence is empty and return empty str if true
#   2.  Initialize an empty list result
#   3.  Split sentence into a list of words using split method
#   4.  Loop through numbers from 1 to 9
#   5.  Loop through words in split_up list
#   6.  Check if number is in word
#   7.  Append word to result list if number is in word
#   8.  Join result list into a str using join method
#   9.  Return sorted str

# -------------------------------------------------------------------------------------
# -----Solution 3-----Javascript Solution-----
# function order(words){
#   return words.split(' ').sort(function(a, b){
#       return a.match(/\d/) - b.match(/\d/);
#    }).join(' ');
# }
# 1.  Split words into an arr of words using split method
# 2.  Sort arr of words using sort method
# 3.  Sort words based on number in word using match method
# 4.  Join sorted arr of words into a str using join method
# 5.  Return sorted str
