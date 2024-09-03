# The male gametes or sperm cells in humans and other mammals are heterogametic 
# and contain one of two types of sex chromosomes. They are either X or Y. The 
# female gametes or eggs however, contain only the X sex chromosome and are 
# homogametic.

# The sperm cell determines the sex of an individual in this case. If a sperm 
# cell containing an X chromosome fertilizes an egg, the resulting zygote will 
# be XX or female. If the sperm cell contains a Y chromosome, then the resulting 
# zygote will be XY or male.

# Determine if the sex of the offspring will be male or female based on the X 
# or Y chromosome present in the male's sperm.

# If the sperm contains the X chromosome, return "Congratulations! You're going 
# to have a daughter."; If the sperm contains the Y chromosome, return 
# "Congratulations! You're going to have a son.";

# -------------------------------------------------------------------------------------
# -----Solution 1-----String Formatting w/ Ternary Operator-----
def chromosome_check(chromosome):
    return 'Congratulations! You\'re going to have a {}.'.format('son' if 'Y' in chromosome else 'daughter')
#   1.  'Y' in chromosome checks if the string chromosome contains the letter 'Y'
#   2.  'son' if 'Y' in chromosome else 'daughter' is a ternary operator that returns 'son' if 'Y' is in 
#       chromosome, otherwise it returns 'daughter'
#   3.  'Congratulations! You\'re going to have a {}.'.format('son' if 'Y' in chromosome else 'daughter') 
#       is a string that uses the .format() method to insert the result of the ternary operator into the string

#   This solution is efficient & easy to understand. It uses the .format() method to insert the result of
#   the ternary operator into the string.

# -------------------------------------------------------------------------------------
# -----Solution 2-----Dictionary Mapping-----
def chromosome_check(chromosome):
    gender = {"XY" : "son", "XX" : "daughter"}
    return "Congratulations! You're going to have a {}.".format(gender[chromosome])
#   1.  A dictionary is used to map the chromosome types to the corresponding offspring gender.
#   2.  Assuming that the chromosome input will always be either "XY" or "XX".

#   Compared to the previous solution, this solution is more readable & easier to understand, but 
#   it requires more memory to store the dictionary. It could fail if input is not exactly 'XY' or 'XX'.

# -------------------------------------------------------------------------------------
# -----Solution 3-----F-String w/ Ternary Operator-----
def chromosome_check(chromosome):
    gender = 'son' if 'Y' in chromosome else 'daughter'
    return f"Congratulations! You're going to have a {chromosome}."
#   1.  'Y' in chromosome checks if the string chromosome contains the letter 'Y'
#   2.  'son' if 'Y' in chromosome else 'daughter' is a ternary operator that returns 'son' if 'Y' is in
#       chromosome, otherwise it returns 'daughter'
#   3.  f"Congratulations! You're going to have a {chromosome}." is an f-string that inserts the value of
#       the chromosome variable into the string

#   This is just as efficient as the first solution, but uses f-strings instead of the .format() method.

# -------------------------------------------------------------------------------------
# -----Solution 4-----Javascript Solution-----
# function chromosomeCheck(chromosome) {
#     return `Congratulations! You're going to have a ${chromosome.includes('Y') ? 'son' : 'daughter'}.`
# }
#   1.  This is the same as the first solution, but written in JavaScript. It uses template literals to
#       insert the result of the ternary operator into the string.

#   This is very readable & concise, similar to the first Python solution w/ the use of template literals.

