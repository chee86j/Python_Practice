# Control Flow Practice Problems

# 1. Check if a number is positive and print a message
number = 5
if number > 0:
    print(f"{number} is positive.")

# 2. Print numbers from 1 to 10 using a for loop
for i in range(1, 11):
    print(i)

# 3. Use a while loop to print five times
counter = 0
while counter < 5:
    print("Iteration", counter + 1)
    counter += 1

# 4. Check if a number is odd or even and print a message
number = 4
if number % 2 == 0:
    print(f"{number} is even.")
else:
    print(f"{number} is odd.")

# 5. Print a 3x3 number grid using nested loops
def create_3x3_grid():
    grid_output = ""
    for i in range(1, 4):
        for j in range(1, 4):
            grid_output += f"({i},{j}) "
        grid_output += "\n"
    return grid_output


# 6. Iterate over a list and print each item
my_list = ["Apple", "Banana", "Cherry"]
for item in my_list:
    print(item)

# 7. Break out of a loop when a condition is met
for i in range(10):
    if i == 5:
        print("Breaking at 5")
        break

# 8. Create a list of squares of numbers 1 to 5
squares = [x**2 for x in range(1, 6)]
print(squares)

# 9. Use range() in a for loop to print numbers
for i in range(5):
    print(f"Number {i}")

# 10. Use an else clause with a for loop
for i in range(3):
    print(i)
else:
    print("Loop completed")
