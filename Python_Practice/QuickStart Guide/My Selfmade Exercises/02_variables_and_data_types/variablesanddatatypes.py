# Variables and Data Types Practice Problems

# Print all data types
int_var = 10  # Integer
str_var = "Hello"  # String
float_var = 10.5  # Float
print("Integer:", int_var, "String:", str_var, "Float:", float_var)

# Swap and print values of two variables
a = 5
b = 10
a, b = b, a  # Swapping values
print("a:", a, "b:", b)

# Convert string to integer and integer to string, then print
str_num = "8"
int_num = 8
converted_str_num = int(str_num)  # String to integer
converted_int_num = str(int_num)  # Integer to string
print("Converted string to integer:", converted_str_num, "Converted integer to string:", converted_int_num)

# Print a list of hobbies
hobbies = ["Reading", "Cycling", "Painting"]
print("Hobbies:", hobbies)

# Calculate and print the average of a list of numbers
numbers = [10, 20, 30, 40, 50]
average = sum(numbers) / len(numbers)
print("Average:", average)

# Explanation: Float vs Integer
# Answer:
#   Floats are numbers with decimal points. Integers are whole numbers 
#   without decimals.

# Create and print a dictionary representing a book
book = {"title": "1984", "author": "George Orwell", "year": 1949}
print("Book:", book)

# Concatenate two strings and print the full sentence
word1 = "Hello"
word2 = "World"
sentence = word1 + " " + word2
print("Sentence:", sentence)

# Print types of various variables
print("Type of int_var:", type(int_var), "Type of str_var:", type(str_var), "Type of float_var:", type(float_var))

# Check and print if a variable is a string
var = "Hello"
is_string = isinstance(var, str)
print("Is 'var' a string?:", is_string)
