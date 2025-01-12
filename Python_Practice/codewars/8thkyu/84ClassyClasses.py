# ===Classy Classes===

# Basic Classes, this kata is mainly aimed at the new JS ES6 Update introducing classes

# ===Task===

# Your task is to complete this Class, the Person class has been created. You must fill in the Constructor 
# method to accept a name as string and an age as number, complete the get Info property and getInfo 
# method/Info getter which should return johns age is 34

# --------------------------------------------------------------------------------------------------------------------------
# -----Solution 1-----@property Decorator & f-string-----
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    @property
    def info(self):
        return '{}s age is {}'.format(self.name, self.age)
    
#   1. __init__ method is used to initialize the object (name, age)
#   2. @property is a decorator that makes a method behave like a read-only attribute
#   3. info method returns the name and age of the person

#   This is a good solution because it uses the @property decorator and f-string to return the name and age of the person
#   It is also a clean and readable solution that has a time complexity of O(1) and a space complexity of O(1)
        
# --------------------------------------------------------------------------------------------------------------------------
# -----Solution 2-----Precomputed String-----
class Person:
    def __init__(self, name, age):
        self.info = f"{name}s age is {age}"
#   1. __init__ method is used to initialize the object (name, age)
#   2. info method returns the name and age of the person

#   Compared to Solution 1, this solution is more concise and uses f-string to return the name and age of the person
#   It is also a clean and readable solution that has a time complexity of O(1) and a space complexity of O(1) with slightly
#   more space usage due to the string being stored directly. There is no need for a getter method because the info 
#   property is already defined in the __init__ method.
    
    
# --------------------------------------------------------------------------------------------------------------------------
# -----Solution 3-----Concatenation in Constructor-----
class Person:
    def __init__(self,name,age):
        self.info=name+"s age is "+str(age)
#   1. __init__ method is used to initialize the object (name, age)
#   2. info method returns the name and age of the person

#   This solution is similar to Solution 2 but uses concatenation to return the name and age of the person
#   It is also a clean and readable solution that has a time complexity of O(1) and a space complexity of O(1). It is less
#   readable than Solution 2 because it uses concatenation instead of f-string.
        
# --------------------------------------------------------------------------------------------------------------------------
# -----Solution 4-----JavaScript Solution-----
# class Person {
#     constructor(name, age) {
#     this.name = name;
#     this.age = age;
#     }
#     get info() {
#     return `${this.name}s age is ${this.age}`;
#     }
# }
#   1. The Person class is defined with a constructor that initializes the name and age of the person
#   2. The info getter method returns the name and age of the person

#   This is a JavaScript solution that uses ES6 syntax to define a class with a constructor and a getter method
#   It is similar to Solution 1 but uses JavaScript syntax instead of Python syntax. The time and space complexity 
#   are the same.
