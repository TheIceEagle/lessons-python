"""
Homework 1: Introduction to Python Basics

Instructions:
1. Complete each function according to the requirements
2. Test your code with the provided test cases
3. Submit a single .py file with all solutions

"""

# Task 1: Number Operations 
def calculate_expressions(a, b):
    """
    Perform basic arithmetic operations with two numbers.
    Return results in a tuple: (sum, difference, product, quotient)
    Handle division by zero by returning None for quotient
    """
    # Your code here
    pass

# Task 2: String Manipulation 
def analyze_string(text):
    """
    Analyze the given string and return a dictionary with:
    - 'length': total characters
    - 'words': number of words
    - 'uppercase': number of uppercase letters
    - 'digits': number of digits
    """
    # Your code here
    pass

# Task 3: List Processing 
def process_list(numbers):
    """
    Process a list of numbers and return a dictionary with:
    - 'even': list of even numbers
    - 'odd': list of odd numbers
    - 'sum': sum of all numbers
    - 'average': average of all numbers (rounded to 2 decimal places)
    """
    # Your code here
    pass


def test_homework():
    # Test Task 1
    print("Task 1 Test:", calculate_expressions(10, 5))  # Should print (15, 5, 50, 2.0)
    
    # Test Task 2
    print("Task 2 Test:", analyze_string("Hello 123 World!"))
    
    # Test Task 3
    print("Task 3 Test:", process_list([1, 2, 3, 4, 5, 6]))

if __name__ == "__main__":
    test_homework()