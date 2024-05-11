# Write Number in Expanded Form
# You will be given a number and you will need to return 
# it as a string in Expanded Form. For example:

# expanded_form(12) # Should return '10 + 2'
# expanded_form(42) # Should return '40 + 2'
# expanded_form(70304) # Should return '70000 + 300 + 4'
# NOTE: All numbers will be whole numbers greater than 0.


# -------------------------------------------------------------------------------------
# -----Solution 1-----Join & List Comprehension & Enumerate & If & For Loop-----
def expanded_form(num):
    num = list(str(num))
    return ' + '.join(x + '0' * (len(num) - y - 1) for y,x in enumerate(num) if x != '0')
#   1.  Convert number to a list of strings
#   2.  Return a string that joins the number and 0's
#   3.  The number is joined with 0's by multiplying the length of the number
#       by the index of the number in the list
#   4.  Each number and its zeros are joined by a '+' sign


# -------------------------------------------------------------------------------------
# -----Solution 2-----Same as Solution 1 but using int instead of str-----
def expanded_form(num):
    return " + ".join([str(int(v)*int("1"+"0"*(len(str(num))-(i+1)))) for i,v in enumerate(str(num)) if v != "0"])
#   1.  Return a string that joins the number and 0's
#   2.  The number is joined with 0's by multiplying the length of the number
#       by the index of the number in the list
#   3.  Each number and its zeros are joined by a '+' sign
#   4.  The number is converted to an integer and multiplied by 1 followed by
#       0's that are subtracted from the length of the number minus the index
#       of the number in the list

# -------------------------------------------------------------------------------------
# -----Solution 3-----divmod(x,y) & For Loop-----
def expanded_form(n):
    result = []
    for a in range(len(str(n)) - 1, -1, -1):
        current = 10 ** a
        quo, n = divmod(n, current)
        if quo:
            result.append(str(quo * current))
    return ' + '.join(result)
#   1.  Initialize an empty list result
#   2.  Loop through the range of the length of the number minus 1 to -1
#       in steps of -1
#   3.  Set current to 10 to the power of a
#   4.  Divide the number by current and set the quotient and remainder to
#       quo and n
#       **Python built-in function divmod(x, y) takes two numbers and returns
#       a pair of numbers consisting of their quotient and remainder**
#   5.  If the quotient is not 0, append the quotient multiplied by current
#       to the result list
#   6.  Return a string that joins the result list with a '+' sign
