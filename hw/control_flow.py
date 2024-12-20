"""
Homework 2: Control Flow and Functions

Instructions:
1. Complete each function according to the requirements
2. Use appropriate control flow statements (if, for, while)
3. Include error handling where specified
4. Test your code with the provided test cases

"""

# Task 1: Grade Calculator (40 points)
def calculate_grade(scores):
    """
    Calculate letter grade based on average of scores.
    Rules:
    - 90-100: 'A'
    - 80-89: 'B'
    - 70-79: 'C'
    - 60-69: 'D'
    - Below 60: 'F'
    Return tuple: (average_score, letter_grade)
    Handle empty list by returning None
    """
    # Your code here
    pass

# Task 2: Password Validator (30 points)
def validate_password(password):
    """
    Validate password strength. Return True if password meets all criteria:
    - At least 8 characters long
    - Contains at least one uppercase letter
    - Contains at least one digit
    - Contains at least one special character (!@#$%^&*)
    Return False otherwise
    """
    # Your code here
    pass

# Task 3: Number Sequence Generator (30 points)
def generate_sequence(start, end, step):
    """
    Generate a list of numbers from start to end (inclusive) with given step.
    Handle cases where:
    - start > end (return empty list)
    - step <= 0 (return None)
    - Invalid input types (return None)
    """
    # Your code here
    pass

# Test cases
def test_homework():
    # Test Task 1
    print("Task 1 Test:", calculate_grade([85, 92, 78, 95, 88]))
    
    # Test Task 2
    print("Task 2 Test:", validate_password("Pass123!"))
    
    # Test Task 3
    print("Task 3 Test:", generate_sequence(1, 10, 2))

if __name__ == "__main__":
    test_homework()