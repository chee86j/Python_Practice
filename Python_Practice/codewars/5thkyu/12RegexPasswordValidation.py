# You need to write regex that will validate a password to make sure 
# it meets the following criteria:

# -At least six characters long
# -contains a lowercase letter
# -contains an uppercase letter
# -contains a digit
# -only contains alphanumeric characters (note that '_' is not alphanumeric)

# -------------------------------------------------------------------------------------
# -----Solution 1-----compile() w/ VERBOSE flag-----
from re import compile, VERBOSE

regex = compile("""
^              # begin word
(?=.*?[a-z])   # at least one lowercase letter
(?=.*?[A-Z])   # at least one uppercase letter
(?=.*?[0-9])   # at least one number
[A-Za-z\d]     # only alphanumeric
{6,}           # at least 6 characters long
$              # end word
""", VERBOSE)

#   This solution uses the re.compile() function to compile the regex pattern. It uses the
#   VERBOSE flag to allow the use of whitespace & comments within the pattern. This makes
#   the pattern more readable. The pattern uses lookahead assertions to check for the presence
#   of at least one lowercase letter, one uppercase letter, & one digit. It then uses a char
#   class to ensure that the password only contains alphanumeric chars. Finally, it uses the
#   {6,} quantifier to ensure that the password is at least 6 chars long.

#   It has a time complexity of O(n) where n is the length of the password & a space complexity
#   of O(1) due to directly using the regex pattern w/o creating any additional data structures.

#   Great for editing & clarity, but not as efficient as the one-liner regex solution.

# -------------------------------------------------------------------------------------
# -----Solution 2-----Compact regex in string form-----
regex = (
    '^'            # start of string
    '(?=.*[a-z])'  # at least one lowercase letter
    '(?=.*[A-Z])'  # at least one uppercase letter
    '(?=.*\d)'     # at least one digit
    '[A-Za-z\d]'   # only alphanumeric characters
    '{6,}'         # at least 6 characters long
    '$'            # end of string
)

#   This solution uses a compact regex pattern in string form. It uses the same logic as Solution
#   1 but without the VERBOSE flag. The pattern uses lookahead assertions to check for the presence
#   of at least one lowercase letter, one uppercase letter, & one digit. It then uses a char class
#   to ensure that the password only contains alphanumeric chars. Finally, it uses the {6,} quantifier
#   to ensure that the password is at least 6 chars long.

#   It has a time complexity of O(n) where n is the length of the password & a space complexity
#   of O(1) due to directly using the regex pattern w/o creating any additional data structures.
#   It is more compact than Solution 1 but less readable & may be unfamilar to those not used to
#   regex patterns.

# -------------------------------------------------------------------------------------
# -----Solution 3-----One-liner regex-----
regex="^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[^\W_]{6,}$"

#   This solution uses a one-liner regex pattern. It uses the same logic as Solutions 1 & 2 but
#   is more compact. The pattern uses lookahead assertions to check for the presence of at least
#   one lowercase letter, one uppercase letter, & one digit
#   It then uses a negated char class [^\W_] to ensure that the password only contains alphanumeric
#   chars. Finally, it uses the {6,} quantifier to ensure that the password is at least 6 chars long.

#   It has a time complexity of O(n) where n is the length of the password & a space complexity
#   of O(1) due to directly using the regex pattern w/o creating any additional data structures.
#   It is the most compact solution & is suitable for those who are familiar with regex patterns.

# -------------------------------------------------------------------------------------
# -----Solution 4-----Javascript Solution-----
# const regex = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[A-Za-z\d]{6,}$/;

# Example usage:
# function validatePassword(password) {
#     return regex.test(password);
# }

# console.log(validatePassword("Abc123")); // true
# console.log(validatePassword("abc")); // false
# console.log(validatePassword("123456")); // false

#   This solution provides a Javascript implementation of the regex pattern. 