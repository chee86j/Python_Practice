# The first input array is the key to the correct answers to an exam, 
# like ["a", "a", "b", "d"]. The second one contains a student's submitted answers.

# The two arrays are not empty and are the same length. Return the score for this 
# array of answers, giving +4 for each correct answer, -1 for each incorrect answer, 
# and +0 for each blank answer, represented as an empty string (in C the space character is used).

# If the score < 0, return 0.

# For example:

#     Correct answer    |    Student's answer   |   Result         
#  ---------------------|-----------------------|-----------
#  ["a", "a", "b", "b"]   ["a", "c", "b", "d"]  →     6
#  ["a", "a", "c", "b"]   ["a", "a", "b", "" ]  →     7
#  ["a", "a", "b", "c"]   ["a", "a", "b", "c"]  →     16
#  ["b", "c", "b", "a"]   ["" , "a", "a", "c"]  →     0

# -------------------------------------------------------------------------------------
# -----Solution 1-----For Loop & If Statements-----
def check_exam(arr1, arr2):
    score = 0
    for i in range(len(arr1)):
        if arr1[i] == arr2[i]:
            score += 4
        elif arr2[i] == "":
            score += 0
        else:
            score -= 1
    return score if score > 0 else 0
#   1. Create a var to store the score
#   2. Loop through the length of the first arr
#   3. Check if the elem in the first arr is equal to the elem in the second arr
#   4. If they are equal, add 4 to the score
#   5. If the elem in the second arr is an empty string, add 0 to the score
#   6. If the elem in the first arr is not equal to the elem in the second arr, subtract 1 from the score
#   7. Return the score if it is greater than 0, otherwise return 0


# -------------------------------------------------------------------------------------
# -----Solution 2-----One Liner w/ List Comprehension & Ternary Operator & Zip-----
def check_exam(arr1, arr2):
    return max(0, sum(4 if a == b else -1 for a, b in zip(arr1, arr2) if b))
#   1. Return the max of 0 and the sum of 4 if a is equal to b else -1 for a, b in the zipped arr1 and arr2 if b
#      zip() is built-in function that takes two iterables and returns an iterator of tuples
#      The iterator generates a series of tuples containing elements from each iterable for example
#      zip([1, 2, 3], [4, 5, 6]) => [(1, 4), (2, 5), (3, 6)]
#   2. If the score is less than 0, return 0


# -------------------------------------------------------------------------------------
# -----Solution 3-----Javascript Solution-----If Statements & For Loop & Ternary Operator-----
# function checkExam(array1, array2) {
#     let score = 0;
#     for (let i = 0; i < array1.length; i++) {
#         if (array1[i] === array2[i]) {
#             score += 4;
#         } else if (array2[i] === "") {
#             score += 0;
#         } else {
#             score -= 1;
#         }
#     }
#     return score > 0 ? score : 0;
# }

#   1. Create a var to store the score
#   2. Loop through the length of the first arr
#   3. Check if the elem in the first arr is equal to the elem in the second arr
#   4. If they are equal, add 4 to the score
#   5. If the elem in the second arr is an empty string, add 0 to the score
#   6. If the elem in the first arr is not equal to the elem in the second arr, subtract 1 from the score
#   7. Return the score if it is greater than 0, otherwise return 0