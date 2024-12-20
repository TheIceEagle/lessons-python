# Python Type Casting Guide

## Basic Type Casting Functions

### 1. Main Type Casting Functions
```python
# str() - Convert to string
str(123)        # => "123"
str(3.14)       # => "3.14"
str(True)       # => "True"

# int() - Convert to integer
int("123")      # => 123
int(3.99)       # => 3 (truncates decimal part)
int("0xFF", 16) # => 255 (hexadecimal)
int(True)       # => 1

# float() - Convert to float
float("3.14")   # => 3.14
float("123")    # => 123.0
float(True)     # => 1.0

# bool() - Convert to boolean
bool(1)         # => True
bool(0)         # => False
bool("Hello")   # => True (non-empty string)
bool("")        # => False (empty string)
bool([])        # => False (empty list)
```

## Common Use Cases

### 1. User Input Processing
```python
# Remember: input() always returns a string
age = input("Enter your age: ")  # Returns "25" as string
age_num = int(age)              # Convert to integer

height = float(input("Enter height in meters: "))  # Direct conversion

# Handling potential errors
try:
    number = int(input("Enter a number: "))
except ValueError:
    print("That's not a valid number!")
```

### 2. Calculations and Data Processing
```python
# String to number conversions
price = "19.99"
quantity = "5"
total = float(price) * int(quantity)  # => 99.95

# Rounding and formatting
result = 3.14159
rounded = int(result)                # => 3
formatted = str(round(result, 2))    # => "3.14"
```

## Practice Exercises

### Exercise 1: Basic Conversions
```python
# Task: Convert these values and print results
num_str = "456"
float_str = "3.14"
bool_str = "True"
zero_str = "0"

# Solution:
num_int = int(num_str)           # => 456
num_float = float(num_str)       # => 456.0
float_num = float(float_str)     # => 3.14
bool_val = bool(bool_str)        # => True
zero_bool = bool(int(zero_str))  # => False
```

### Exercise 2: Temperature Converter
```python
def convert_temperature():
    # Get Celsius temperature from user and convert to Fahrenheit
    celsius = input("Enter temperature in Celsius: ")
    try:
        celsius_float = float(celsius)
        fahrenheit = (celsius_float * 9/5) + 32
        print(f"{celsius}°C is {fahrenheit}°F")
    except ValueError:
        print("Please enter a valid number")

# Example usage:
# Enter temperature in Celsius: 25
# 25°C is 77.0°F
```

### Exercise 3: Grade Calculator
```python
def calculate_grade():
    scores = []
    for i in range(3):
        while True:
            try:
                score = float(input(f"Enter score {i+1}: "))
                if 0 <= score <= 100:
                    scores.append(score)
                    break
                else:
                    print("Score must be between 0 and 100")
            except ValueError:
                print("Please enter a valid number")
    
    average = sum(scores) / len(scores)
    return round(average, 2)

# Example usage:
# Enter score 1: 85.5
# Enter score 2: 90
# Enter score 3: 88.5
# Average: 88.0
```

## Common Pitfalls and Solutions

### 1. Handling Invalid Conversions
```python
# Wrong way:
number = int("abc")  # Raises ValueError

# Right way:
try:
    number = int("abc")
except ValueError:
    print("Invalid number format")
```

### 2. Boolean Conversion Rules
```python
# Understanding what converts to False
print(bool(""))      # False (empty string)
print(bool([]))      # False (empty list)
print(bool({}))      # False (empty dict)
print(bool(0))       # False
print(bool(None))    # False

# Everything else converts to True
print(bool("0"))     # True (non-empty string)
print(bool([0]))     # True (non-empty list)
print(bool(-1))      # True
```

### 3. Number Format Handling
```python
def safe_convert_number(value):
    """Safely convert string to number (int or float)"""
    try:
        # Try converting to int first
        return int(value)
    except ValueError:
        try:
            # If int fails, try float
            return float(value)
        except ValueError:
            return None

# Example usage:
print(safe_convert_number("123"))    # => 123 (int)
print(safe_convert_number("12.34"))  # => 12.34 (float)
print(safe_convert_number("abc"))    # => None
```

## Homework Exercises

### 1. Shopping Cart Calculator
```text

Create a program that:
1. Asks for item prices as strings
2. Converts them to floats
3. Calculates total
4. Handles invalid inputs

# Solution test:
# Enter price: 12.99
# Enter price: 5.50
# Enter price: abc (Invalid price, please try again)
# Enter price: done
# Total: 18.49
```

### 2. Number System Converter
```text

Create a program that converts numbers between different bases
(decimal, binary, hexadecimal)




# Solution test:
# Enter a decimal number: 255
# Binary: 0b11111111
# Hexadecimal: 0xff
# Octal: 0o377
```
