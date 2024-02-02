# Data Structures Practice Problems

# 1. Print all fruits in the list
fruits = ["Apple", "Banana", "Cherry", "Date", "Elderberry"]
print("All fruits:", fruits)

# 2. Update the fruits list: add 'Fig' and remove 'Banana'
fruits.append("Fig")
fruits.remove("Banana")
print("Updated fruits list:", fruits)

# 3. Find and print the largest number in the numbers list
numbers = [10, 30, 25, 40, 15]
largest_number = max(numbers)
print("Largest number:", largest_number)

# 4. Manipulate a tuple containing mixed data types
my_tuple = (1, "Hello", 3.14)
# Example operation: print each element in the tuple
for element in my_tuple:
    print(element)

# 5. Explain the difference between a list and a tuple
# Answer:
#   A list is mutable, allowing changes (add, remove, modify). 
#   A tuple is immutable; once created, it can't be changed.

# 6. Demonstrate union and intersection with sets
set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1 | set2
intersection_set = set1 & set2
print("Union:", union_set, "Intersection:", intersection_set)

# 7. Count and print the frequency of each character in a string
my_string = "banana"
frequency = {char: my_string.count(char) for char in set(my_string)}
print("Character frequencies:", frequency)

# 8. Map countries to their capitals and print
countries = {"USA": "Washington D.C.", "Japan": "Tokyo", "France": "Paris"}
print("Countries and their capitals:", countries)

# 9. Reverse a list and print it
my_list = [1, 2, 3, 4, 5]
my_list.reverse()
print("Reversed list:", my_list)

# 10. Access and print an element from a nested dictionary
nested_dict = {"dict1": {"key1": 1, "key2": 2}, "dict2": {"key3": 3, "key4": 4}}
print("Element from nested dictionary:", nested_dict["dict1"]["key2"])
