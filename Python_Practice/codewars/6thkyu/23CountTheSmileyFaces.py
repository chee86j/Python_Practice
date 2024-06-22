# Given an array (arr) as an argument complete the function c
# ountSmileys that should return the total number of smiling faces.

# Rules for a smiling face:

# Each smiley face must contain a valid pair of eyes. Eyes can be 
# marked as : or ;
# A smiley face can have a nose but it does not have to. Valid 
# characters for a nose are - or ~
# Every smiling face must have a smiling mouth that should be 
# marked with either ) or D
# No additional characters are allowed except for those mentioned.

# Valid smiley face examples: :) :D ;-D :~)
# Invalid smiley faces: ;( :> :} :]

# Example
# countSmileys([':)', ';(', ';}', ':-D']);       // should return 2;
# countSmileys([';D', ':-(', ':-)', ';~)']);     // should return 3;
# countSmileys([';]', ':[', ';*', ':$', ';-D']); // should return 1;
# Note
# In case of an empty array return 0. You will not be tested with 
# invalid input (input will always be an array). Order of the face 
# (eyes, nose, mouth) elements will always be the same.


# -------------------------------------------------------------------------------------
# -----Solution 1-----List & Loop & Count-----
def count_smileys(arr):
    eyes = [":", ";"]
    noses = ["", "-", "~"]
    mouths = [")", "D"]
    count = 0
    for eye in eyes:
        for nose in noses:
            for mouth in mouths:
                face = eye + nose + mouth
                count += arr.count(face)
    return count
#   1. The function takes in an arr of strings.
#   2. Three lists are created to store the possible eyes, noses,
#      and mouths of a smiley face.
#   3. A variable count is initialized to 0.
#   4. Three nested loops are used to iterate through the eyes,
#      noses, and mouths.
#   5. A face is created by concatenating the eye, nose, and mouth.
#   6. The count of the face in the arr is added to the count
#      variable.
#   7. The count variable is returned.

# -------------------------------------------------------------------------------------
# -----Solution 2-----Regex-----
from re import findall
def count_smileys(arr):
    return len(list(findall(r"[:;][-~]?[)D]", " ".join(arr))))
#   1. The function takes in an arr of strings.
#   2. The strings are joined together with a space in between.
#   3. The findall method is used to find all the strings that
#      match the regex pattern.
#   4. The regex pattern checks for strings that start with either
#      a colon or a semicolon, followed by an optional nose, and
#      ends with either a closing parenthesis or a capital D.
#   5. The findall method returns a list of all the strings that
#      match the pattern.

# -------------------------------------------------------------------------------------
# -----Solution 3-----Javascript Solution-----Regex
# function countSmileys(arr) {
#     return arr.filter(x => /^[:;][-~]?[)D]$/.test(x)).length;
#     }

#   1. The function takes in an arr of strings.
#   2. The filter method is used to filter out the strings that
#      match the regex pattern.
#   3. The regex pattern checks for strings that start with either
#      a colon or a semicolon, followed by an optional nose, and
#      ends with either a closing parenthesis or a capital D.
#   4. The length of the filtered arr is returned.
