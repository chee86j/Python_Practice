# Move the first letter of each word to the end of it, 
# then add "ay" to the end of the word. Leave punctuation 
# marks untouched.
# Examples

# pig_it('Pig latin is cool') # igPay atinlay siay oolcay
# pig_it('Hello world !')     # elloHay orldway !

# -------------------------------------------------------------------------------------
# -----Solution 1-----Split & Join & List Comprehension & String Slicing & isalpha-----
def pig_it(text):
    lst = text.split()
    return ' '.join( [word[1:] + word[:1] + 'ay' if word.isalpha() else word for word in lst])
#  1. Split the text into a list of words
#  2. Iterate over the list of words
#  3. If the word is a letter, slice the first letter and add it to the end with 'ay'
#  4. If the word is not a alphabet, leave it as it is
#  5. Join the list of words back into a string and return it

#  Example:
#  1. 'Pig latin is cool'.split() => ['Pig', 'latin', 'is', 'cool']
#  2. [word[1:] + word[:1] + 'ay' if word.isalpha() else word for word in lst] => ['igPay', 'atinlay', 'siay', 'oolcay']
#  3. ' '.join(['igPay', 'atinlay', 'siay', 'oolcay']) => 'igPay atinlay siay oolcay'

# -------------------------------------------------------------------------------------
# -----Solution 2-----Join & String Slicing & isalnum & Split-----
def pig_it(text):
    return " ".join(x[1:] + x[0] + "ay" if x.isalnum() else x for x in text.split())
#  1. Split the text into a list of words
#  2. Iterate over the list of words
#  3. Check if 'x' is a letter or a number
#  4. If 'x' is a letter, slice the first letter and add it to the end with 'ay'
#  5. If 'x' is not a letter, leave it as it is
#  6. Join the list of words back into a string and return it

#  Example:
#  1. 'Pig latin is cool'.split() => ['Pig', 'latin', 'is', 'cool']
#  2. [" ".join(x[1:] + x[0] + "ay" if x.isalnum() else x for x in text.split()] => 'igPay atinlay siay oolcay'


# -------------------------------------------------------------------------------------
# -----Solution 3-----For Loop & List & Append & isalpha & Join-----
def pig_it(text):
    res = []
    
    for i in text.split():
        if i.isalpha():
            res.append(i[1:]+i[0]+'ay')
        else:
            res.append(i)
            
    return ' '.join(res)
#  1. Split the text into a list of words
#  2. Iterate over the list of words
#  3. Check if 'i' is a letter
#  4. If 'i' is a letter, slice the first letter and add it to the end with 'ay'
#  5. If 'i' is not a letter, leave it as it is
#  6. Append the word to the list 'res'
#  7. Join the list of words back into a string and return it

#  Example:
#  1. 'Pig latin is cool'.split() => ['Pig', 'latin', 'is', 'cool']
#  2. ['igPay', 'atinlay', 'siay', 'oolcay']

# -------------------------------------------------------------------------------------
# -----Solution 4-----Javascript Solution-----
# function pigIt(str){
#     return str.split(' ').map(function(el){
#         return el.slice(1) + el.slice(0,1) + 'ay';
#     }).join(' ');
# }

#  1. Split the str into an arr of words
#  2. Map over the arr
#  3. For each word, slice off the first letter, add it to the end, and add 'ay'
#  4. Join the arr back into a str and return it

#  Example:
#  1. 'Pig latin is cool'.split(' ') => ['Pig', 'latin', 'is', 'cool']
#  2. ['Pig', 'latin', 'is', 'cool'].map(function(el){
#         return el.slice(1) + el.slice(0,1) + 'ay';
#     }) => ['igPay', 'atinlay', 'siay', 'oolcay']
#  3. ['igPay', 'atinlay', 'siay', 'oolcay'].join(' ') => 'igPay atinlay siay oolcay'


