# Grade book
# Complete the function so that it finds the average of the three scores passed to it and returns the letter value associated with that grade.

# Numerical Score	Letter Grade
# 90 <= score <= 100	'A'
# 80 <= score < 90	'B'
# 70 <= score < 80	'C'
# 60 <= score < 70	'D'
# 0 <= score < 60	'F'
# Tested values are all between 0 and 100. Theres is no need to check for negative values or values greater than 100.

# -------------------------------------------------------------------------------------
# -----Solution 1-----If-elif-else statement-----
# Solution 1
def get_grade(s1, s2, s3):
    # Calculate  avg of three scores
    average = (s1 + s2 + s3) / 3
    
    # Determine letter grade based on avg score
    if 90 <= average <= 100:
        return 'A'
    elif 80 <= average < 90:
        return 'B'
    elif 70 <= average < 80:
        return 'C'
    elif 60 <= average < 70:
        return 'D'
    else:
        return 'F'

# -------------------------------------------------------------------------------------
# -----Solution 2-----If w/Ternary Operator-----
def get_grade(s1, s2, s3):
    # Calculate mean of three scores
    mean = sum([s1,s2,s3]) / 3
    
    # Use Ternary Operator to determine letter grade based on mean score
    if mean >= 90: return 'A'
    if mean >= 80: return 'B'
    if mean >= 70: return 'C'
    if mean >= 60: return 'D'
    return 'F'

# -------------------------------------------------------------------------------------
# -----Solution 3-----Dictionary to Map avg score to letter grade-----
# Use a dictionary to map the average score to corresponding letter grade
    # The average score is obtained by dividing sum of the scores by 30
    # If average score is not in the dictionary, return 'F'
    return {6: 'D', 7: 'C', 8: 'B', 9: 'A', 10: 'A'}.get((s1 + s2 + s3) // 30, 'F')