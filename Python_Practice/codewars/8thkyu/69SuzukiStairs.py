# Suzuki is a monk who climbs a large staircase to the monastery 
# as part of a ritual. Some days he climbs more stairs than others 
# depending on the number of students he must train in the morning. 
# He is curious how many stairs might be climbed over the next 
# 20 years and has spent a year marking down his daily progress.

# The sum of all the stairs logged in a year will be used for 
# estimating the number he might climb in 20.

# 20_year_estimate = one_year_total * 20

# You will receive the following data structure representing 
# the stairs Suzuki logged in a year. You will have all data 
# for the entire year so regardless of how it is logged the 
# problem should be simple to solve.

# stairs = [sunday,monday,tuesday,wednesday,thursday,friday,saturday]

# Make sure your solution takes into account all of the nesting within 
# the stairs array.

# Each weekday in the stairs array is an array.

# sunday = [6737, 7244, 5776, 9826, 7057, 9247, 5842, 5484, 6543, 5153, 
#           6832, 8274, 7148, 6152, 5940, 8040, 9174, 7555, 7682, 5252, 
#           8793, 8837, 7320, 8478, 6063, 5751, 9716, 5085, 7315, 7859, 
#           6628, 5425, 6331, 7097, 6249, 8381, 5936, 8496, 6934, 8347, 
#           7036, 6421, 6510, 5821, 8602, 5312, 7836, 8032, 9871, 5990, 
#           6309, 7825]

# Your function should return the 20 year estimate of the stairs 
# climbed using the formula above. 

# -------------------------------------------------------------------------------------
# -----Solution 1-----One-Liner w/List Comprehension-----
def stairs_in_20(stairs):
    return sum(sum(day) for day in stairs) * 20
#   1. This () takes one argument stairs.
#   2. It then iterates through the list of days in the stairs arr. `for day in stairs`
#   3. The sum of the stairs climbed on each day is then calculated. `sum(day)`
#   4. The sum of the stairs climbed in a yr is then calculated. `sum(sum(day) for day 
#      in stairs)`
#   5. The 20 yr estimate of the stairs climbed is then calculated. `sum(sum(day) for day 
#      in stairs) * 20`
#   6. The final result is then returned.

#   This solution's space complexity is O(1) because we are not using any additional 
#   data structures using a constant amount of space. This solution is the most efficient 
#   in terms of time complexity (O(n)) as it iterates through all the days in the list to
#   find the total stairs climbed in a yr.

# -------------------------------------------------------------------------------------
# -----Solution 2-----Map-----
def stairs_in_20(stairs):
    return 20 * sum(map(sum, stairs))
#   1. This () takes one argument stairs.
#   2. The map() function is then used to iterate through the list of days in the stairs arr.
#   3. The sum of the stairs climbed on each day is then calculated. `sum`
#   4. The sum of the stairs climbed in a yr is then calculated. `map(sum, stairs)`
#   5. The 20 yr estimate of the stairs climbed is then calculated. `sum(map(sum, stairs)) * 20`
#   6. The final result is then returned.

#   Like Solution 1, it doesn't use any additional data structures using a constant amount 
#   of space. Using the map() is efficient because it avoids the overhead of creating 
#   a list of intermediate results. The time complexity of this solution is O(n) because
#   the map() function iterates through all the days in the list to find the total stairs
#   climbed in a yr.
 
# -------------------------------------------------------------------------------------
# -----Solution 3-----For Loop-----
def stairs_in_20(stairs):
    tot = 0
    for d in stairs:
        for s in d:
            tot += s
    return tot * 20
#   1. This () takes one argument stairs.
#   2. A variable tot is initialized to 0.
#   3. The outer loop iterates through the list of days in the stairs arr. `for d in stairs`
#   4. The inner loop iterates through the list of stairs climbed on each day. `for s in d`
#   5. The total stairs climbed is then calculated. `tot += s`
#   6. The 20 yr estimate of the stairs climbed is then calculated. `tot * 20`
#   7. The final result is then returned.

#   This solution's space complexity is O(1) because we are not using any additional data 
#   structures using a constant amount of space. This solution is the least efficient in
#   terms of time complexity (O(n^2)) as it iterates through all the days in the list to
#   find the total stairs climbed in a yr. This is more verbose than the previous solutions, 
#   but is easier to understand for beginners.

# -------------------------------------------------------------------------------------
# -----Solution 4-----Javascript Solution-----
# function stairsIn20(a) {
#   return 20 * a.reduce((s, a) => s + a.reduce((s, n) => s + n, 0), 0);
# }

#   1. This function takes one argument a.
#   2. The reduce() function is then used to iterate through the list of days in the 
#      stairs arr.
#   3. The reduce() function is then used to iterate through the list of stairs climbed
#      on each day.
#   4. The total stairs climbed is then calculated.
#   5. The 20 yr estimate of the stairs climbed is then calculated.
#   6. The final result is then returned.

#   This is the equivalent of Solution 2 in Python. The reduce() function is used to 
#   iterate through the list of days in the stairs arr. The time complexity of this
#   solution is O(n) because the reduce() function iterates through all the days in
#   the list to find the total stairs climbed in a yr. This solution is more efficient 
#   using the reduce() as it iterates over all elements in the arr.
