# John & Mary want to travel between a few towns A, B, C ... Mary has on a sheet 
# of paper a list of distances between these towns. ls = [50, 55, 57, 58, 60]. John 
# is tired of driving & he says to Mary that he doesn't want to drive more than 
# t = 174 miles & he will visit only 3 towns.

# Which distances, hence which towns, they will choose so that the sum of the 
# distances is the biggest possible to please Mary & John?

# Example:

# With list ls & 3 towns to visit they can make a choice between: 
# [50,55,57],[50,55,58],[50,55,60],[50,57,58],[50,57,60],[50,58,60],[55,57,58],[55,57,60],[55,58,60],[57,58,60].

# The sums of distances are then: 162, 163, 165, 165, 167, 168, 170, 172, 173, 175.

# The biggest possible sum taking a limit of 174 into account is then 173 & the 
# distances of the 3 corresponding towns is [55, 58, 60].

# The function chooseBestSum (or choose_best_sum or ... depending on the language) 
# will take as parameters t (maximum sum of distances, integer >= 0), k (number of 
# towns to visit, k >= 1) & ls (list of distances, all distances are positive or 
# zero integers & this list has at least one element). The function returns the 
# "best" sum ie the biggest possible sum of k distances less than or equal to the 
# given limit t, if that sum exists, or otherwise nil, null, None, Nothing, depending 
# on the language. In that case with C, C++, D, Dart, Fortran, F#, Go, Julia, Kotlin, 
# Nim, OCaml, Pascal, Perl, PowerShell, Reason, Rust, Scala, Shell, Swift return -1.

# Examples:
# ts = [50, 55, 56, 57, 58] choose_best_sum(163, 3, ts) -> 163

# xs = [50] choose_best_sum(163, 3, xs) -> nil (or null or ... or -1 (C++, C, D, Rust, Swift, Go, ...)

# ys = [91, 74, 73, 85, 73, 81, 87] choose_best_sum(230, 3, ys) -> 228

# Notes:
# try not to modify the input list of distances ls
# in some languages this "list" is in fact a string (see the Sample Tests).

# -------------------------------------------------------------------------------------
# Logic:
    # 1. A max limit t (the maximum sum of distances John can driver)
    # 2. A required number k(the number of towns to visit)
    # 3. A list of distances between towns ls

    # You need to:
    # 1. Select k distances from the list ls
    # 2. Ensure their sum is less than or equal to t
    # 3. Find the largest possible sum that satisfies the above conditions

# -------------------------------------------------------------------------------------
# -----Solution 1-----Using itertools.combinations with max()----------Using
import itertools
def choose_best_sum(t, k, ls):
    try: 
        return max(sum(i) for i in itertools.combinations(ls,k) if sum(i)<=t)
    except:
        return None
# 1. We start by importing the itertools module, which contains the combinations() function.
# 2. We then use a try-except block to h&le the case where no combination of distances satisfies the conditions.
# 3. We use a generator expression to generate all possible combinations of k distances from the list ls.
# 4. We then use the max() function to find the largest sum of distances that is less than or equal to t.
# 5. If no such sum exists, we return None.

# The time complexity of this solution is O(n^k), where n is the number of distances in the list ls & k is the number 
# of towns to visit. This is because we are generating all possible combinations of k distances from the list ls.
# The space complexity is O(1) as we are not using any additional data structures that grow with the input size.

# This is a straightforward & readable solution, but inefficient for large n or k due to the need to generate
# all possible combinations of distances. The try-except for h&ling where no combination satisfies the conditions
# is a nice touch, but it could be improved by using a default value for max() instead of catching an exception.

# -------------------------------------------------------------------------------------
# -----Solution 2-----Using Nested List Generator-----
from itertools import combinations

def choose_best_sum(t, k, ls):
    return max((s for s in (sum(dists) for dists in combinations(ls, k)) if s <= t), default=None)
# 1. We start by importing the combinations() function from the itertools module.
# 2. We use a nested list generator to generate all possible combinations of k distances from the list ls.
# 3. We then use another generator expression to calculate the sum of distances for each combination.
# 4. We filter out combinations where the sum of distances is greater than t.
# 5. Finally, we use the max() function to find the largest sum of distances that is less than or equal to t.

# The time complexity of this solution is O(n choose k), where n is the number of distances in the list ls & k is the
# number of towns to visit. This is because we are generating all possible combinations of k distances from the list ls.
# The space complexity is O(1) as we are not using any additional data structures that grow with the input size.

# This solution is similar to the previous one but uses a nested list generator instead of a try-except block to h&le
# the case where no combination satisfies the conditions. It is more efficient than the previous solution as it avoids
# the overhead of exception h&ling.

# -------------------------------------------------------------------------------------
# -----Solution 3-----Alternative Nested List Generator-----
from itertools import combinations

def choose_best_sum(t, k, ls):
    return max((sum(v) for v in combinations(ls,k) if sum(v)<=t), default=None)
# 1. We start by importing the combinations() function from the itertools module.
# 2. We use a nested list generator to generate all possible combinations of k distances from the list ls.
# 3. We then use another generator expression to calculate the sum of distances for each combination.
# 4. We filter out combinations where the sum of distances is greater than t.
# 5. Finally, we use the max() function to find the largest sum of distances that is less than or equal to t.

# The time complexity of this solution is O(n choose k), where n is the number of distances in the list ls & k is the
# number of towns to visit. This is because we are generating all possible combinations of k distances from the list ls.
# The space complexity is O(1) as we are not using any additional data structures that grow with the input size.

# This solution is similar to the previous one but uses a more concise generator expression to calculate the sum of
# distances for each combination. It is efficient & easy to read, making it a good choice for this problem.

# -------------------------------------------------------------------------------------
# -----Solution 3-----Using Recursion----------
def choose_best(t,k,ls):
    if k == 0: return 0
    best = -1
    for i, v in enumerate(ls):
        if v > t: continue
        b = choose_best(t - v, k - 1, ls[i+1:])
        if b < 0: continue
        b += v
        if b > best & b <= t:
            best = b
    return best

def choose_best_sum(t, k, ls):
    c = choose_best(t,k,ls)
    if c <= 0 : return None
    return c
# 1. We define a recursive function choose_best() that takes the current sum t, the number of towns k, & the list of distances ls as arguments.
# 2. The base case of the recursion is when k is 0, in which case we return 0.
# 3. We initialize a variable best to store the best sum of distances found so far.
# 4. We iterate over the distances in the list ls, skipping any distance greater than t.
# 5. For each distance v, we recursively call choose_best() with the updated sum t - v, the reduced number of towns k - 1, & the remaining distances ls[i+1:].
# 6. If the recursive call returns a valid sum b, we add the current distance v to it.
# 7. We update the best sum if the new sum is greater than the current best & less than or equal to t.
# 8. Finally, we return the best sum found by the recursive calls.
# 9. We define the choose_best_sum() function that calls choose_best() & returns the best sum if it is greater than 0, or None otherwise.

# The time complexity of this solution is O(n choose k), where n is the number of distances in the list ls & k is the number of towns to visit.
# This is because we are exploring all possible combinations of k distances from the list ls using recursion.
# The space complexity is O(k) due to the recursive calls, where k is the number of towns to visit.

# This solution may be slower for large inputs, harder to read, but more memory-efficient than the previous solutions.

# -------------------------------------------------------------------------------------
# -----Solution 4-----JavaScript Solution----
# function chooseBestSum(t, k, ls) {
#     if (k > ls.length) return null;

#     const combinations = (arr, k) => {
#         if (k === 0) return [[]];
#         if (arr.length === 0) return [];
#         const [first, ...rest] = arr;
#         const withFirst = combinations(rest, k - 1).map(combo => [first, ...combo]);
#         const withoutFirst = combinations(rest, k);
#         return [...withFirst, ...withoutFirst];
#     };

#     const combos = combinations(ls, k);
#     const validSums = combos.map(combo => combo.reduce((a, b) => a + b, 0)).filter(sum => sum <= t);
#     return validSums.length ? Math.max(...validSums) : null;
# }
# 1. We define the chooseBestSum() function that takes the maximum sum t, the number of towns k, & the list of distances ls as arguments.
# 2. We check if the number of towns k is greater than the length of the list ls & return null if it is.
# 3. We define a helper function combinations() that generates all possible combinations of k distances from the list ls.
# 4. The combinations() function uses a recursive approach to generate combinations of k distances.
# 5. We calculate the sum of distances for each combination & filter out sums greater than t.
# 6. We return the largest valid sum of distances or null if no valid sum is found.

