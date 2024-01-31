# 1. We start by creatina  file called math_functions.py that 
#    contains the functions we want to test.

# 2. Then we create a file called test_math_functions.py in order
#    to write our test cases.

# 3. We import the unittest module and the functions we want to test
#    from the math_functions module.

# 4. To run the tests, we use the unittest.main() function, and in the
#    command line we run the test_math_functions.py file with the command
#    'python test_math_functions.py.'

# your_project/
# │
# ├── math_functions.py       # File containing functions to test
# └── test_math_functions.py  # File containing unittest test cases

# Tips

#     *Each test method in your unittest.TestCase subclass should start with the word test. 
#     This naming convention informs the test runner about which methods represent tests.
#     *Use assert methods provided by unittest.TestCase, such as assertEqual, assertTrue, 
#     assertFalse, to check the behavior of your functions.
#     *You can have multiple test cases (methods) within a single test class, and you can 
#     have multiple test classes in a test file.


def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

