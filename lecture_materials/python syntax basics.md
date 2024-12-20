# Comprehensive Python Programming Tutorial

## Table of Contents
1. [Development Environment Setup](#development-environment-setup)
2. [Python Fundamentals](#python-fundamentals)
3. [Variables and Data Types](#variables-and-data-types)
4. [Control Flow](#control-flow)
5. [Functions](#functions)
6. [Collections and Data Structures](#collections-and-data-structures)
7. [Modules](#modules)
8. [File Operations](#file-operations)
9. [Practice Projects](#practice-projects)

## Development Environment Setup
### 1. Installing Python
1. Visit [python.org](https://python.org)
2. Download the latest version for your OS
3. During installation on Windows:
   - ✅ Check "Add Python to PATH"
   - ✅ Check "Install pip"
4. Verify installation:
```bash
python --version
pip --version
```

### 2. IDE Installation

#### PyCharm Community Edition
1. Visit [jetbrains.com/pycharm](https://jetbrains.com/pycharm)
2. Download Community Edition
3. Install with default settings
4. First launch setup:
   - Select dark/light theme
   - Install recommended plugins

#### VS Code Setup
1. Install VS Code from [code.visualstudio.com](https://code.visualstudio.com)
2. Install Python extension:
   - Open VS Code
   - Go to Extensions (Ctrl+Shift+X)
   - Search "Python"
   - Install Microsoft's Python extension

## Virtual Environments

### What is a Virtual Environment?
A virtual environment is an isolated Python environment that allows you to install packages specifically for your project without affecting other projects or the global Python installation.

### Creating and Using Virtual Environments

#### Using venv (Built-in)
```bash
# Windows
python -m venv myenv
myenv\Scripts\activate

# macOS/Linux
python3 -m venv myenv
source myenv/bin/activate

# Deactivate (all platforms)
deactivate
```

#### Using virtualenv (Alternative)
```bash
# Install virtualenv
pip install virtualenv

# Create environment
virtualenv myenv

# Activate
# Windows
myenv\Scripts\activate
# macOS/Linux
source myenv/bin/activate
```

### Best Practices
1. Create one virtual environment per project
2. Add virtual environment directory to .gitignore
3. Activate virtual environment before installing packages
4. Keep environments clean - only install necessary packages

## Package Management

### Requirements File

#### Creating requirements.txt
```bash
# Manually create
touch requirements.txt

# Or automatically generate from current environment
pip freeze > requirements.txt
```

#### Sample requirements.txt
```text
numpy==1.21.0
pandas==1.3.0
requests==2.26.0
python-dotenv==0.19.0
```

#### Installing from requirements.txt
```bash
pip install -r requirements.txt
```

### Common Project Structure
```
project_name/
│
├── myenv/              # Virtual environment
├── src/               # Source code
│   ├── __init__.py
│   ├── main.py
│   └── utils.py
│
├── tests/             # Test files
│   ├── __init__.py
│   └── test_main.py
│
├── data/              # Data files
├── docs/              # Documentation
├── requirements.txt   # Project dependencies
├── README.md         # Project documentation
└── .gitignore        # Git ignore file
```


## Python Fundamentals

### Comments
```python
# Single line comment

"""
Multi-line comment
or documentation string
"""
```

### Basic Operations
```python
# Basic arithmetic
1 + 1    # => 2
8 - 1    # => 7
10 * 2   # => 20
35 / 5   # => 7.0  (division always returns float)

# Floor division (rounds down)
5 // 3       # => 1
-5 // 3      # => -2
5.0 // 3.0   # => 1.0

# Modulo operation
7 % 3    # => 1
-7 % 3   # => 2 (result has same sign as divisor)

# Exponentiation
2 ** 3   # => 8

# Order of operations with parentheses
1 + 3 * 2    # => 7
(1 + 3) * 2  # => 8
```

### Boolean Operations
```python
# Boolean values are capitalized
True and False  # => False
False or True   # => True
not True        # => False

# Boolean operations with numbers
bool(0)     # => False
bool("")    # => False
bool([])    # => False
bool(42)    # => True

# Comparison operators
1 == 1      # => True
2 != 1      # => True
1 < 10      # => True
1 <= 1      # => True
1 > 10      # => False
```

## Variables and Data Types

### String Operations
```python
# String creation
name = "Python"
multi_line = """Multiple
lines"""

# String concatenation
"Hello" + " World"    # => "Hello World"
"Hello " "World"      # => "Hello World"

# String formatting
name = "Alice"
age = 25
f"{name} is {age} years old"    # => "Alice is 25 years old"
"{} is {}".format(name, age)    # => "Alice is 25 years old"

# String operations
len("Python")          # => 6
"Python"[0]           # => "P"
"Python".upper()      # => "PYTHON"
"Python".lower()      # => "python"
"  Python  ".strip()  # => "Python"
```

### Numbers
```python
# Integer operations
x = 5
y = 3
x + y      # => 8
x - y      # => 2
x * y      # => 15
x / y      # => 1.6666...
x // y     # => 1 (floor division)
x % y      # => 2 (modulo)
x ** y     # => 125 (exponentiation)

# Float operations
pi = 3.14159
round(pi, 2)    # => 3.14
abs(-pi)        # => 3.14159
```

## Collections and Data Structures

### Lists
```python
# Creating lists
empty_list = []
numbers = [1, 2, 3, 4, 5]

# List operations
numbers.append(6)       # Add item
numbers.remove(6)      # Remove item
numbers.insert(0, 0)   # Insert at position
numbers.pop()          # Remove and return last item
len(numbers)          # Get length
numbers[0]            # Access first item
numbers[-1]           # Access last item
numbers[1:3]          # Slice list
numbers.extend([6,7])  # Add multiple items

# List comprehension
squares = [x**2 for x in range(5)]  # => [0, 1, 4, 9, 16]
```

### Tuples
```python
# Creating tuples (immutable)
point = (1, 2)
single = (1,)      # Note the comma
empty = ()

# Tuple operations
x, y = point       # Unpacking
len(point)         # => 2
point[0]           # => 1
```

### Dictionaries
```python
# Creating dictionaries
empty_dict = {}
person = {
    "name": "Alice",
    "age": 25,
    "city": "Wonderland"
}

# Dictionary operations
person["name"]                  # Access value
person.get("age", 0)           # Access with default
person.update({"age": 26})     # Update value
list(person.keys())            # Get keys
list(person.values())          # Get values
"name" in person               # Check key existence
```

### Sets
```python
# Creating sets
empty_set = set()
numbers = {1, 2, 3, 4, 5}
duplicates = {1, 1, 2, 2, 3}   # => {1, 2, 3}

# Set operations
numbers.add(6)                  # Add item
numbers.remove(6)               # Remove item
{1, 2, 3} & {2, 3, 4}          # Intersection
{1, 2, 3} | {2, 3, 4}          # Union
{1, 2, 3} - {2, 3}             # Difference
```

## Control Flow

### If Statements
```python
if condition:
    print("True")
elif other_condition:
    print("Other")
else:
    print("False")

# Ternary operator
result = "Yes" if condition else "No"
```

### Loops
```python
# For loops
for i in range(5):
    print(i)

# For loop with enumeration
for index, value in enumerate(["a", "b", "c"]):
    print(f"{index}: {value}")

# While loops
count = 0
while count < 5:
    print(count)
    count += 1
```

### Exception Handling
```python
try:
    # Risky operation
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")
except Exception as e:
    print(f"Error: {e}")
else:
    print("No error occurred")
finally:
    print("This always runs")
```

## Functions

### Basic Functions
```python
# Function definition
def greet(name):
    return f"Hello, {name}!"

# Function with default parameters
def greet(name="World"):
    return f"Hello, {name}!"

# Multiple returns
def divide(a, b):
    if b == 0:
        return None
    return a / b

# Lambda functions
square = lambda x: x**2
```

### Advanced Function Features
```python
# Variable arguments
def sum_all(*args):
    return sum(args)

# Keyword arguments
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# Combining both
def combined(*args, **kwargs):
    print(f"Args: {args}")
    print(f"Kwargs: {kwargs}")
```

## Modules

### Import Operations
```python
# Basic import
import math
math.sqrt(16)    # => 4.0

# Import specific functions
from math import sqrt, pi
sqrt(16)         # => 4.0

# Import with alias
import math as m
m.sqrt(16)       # => 4.0

# Import all (not recommended)
from math import *
```


## Best Practices

1. **Code Style**
   - Follow PEP 8 guidelines
   - Use meaningful variable names
   - Add appropriate comments
   - Consistent indentation (4 spaces)

2. **Error Handling**
   - Use try/except appropriately
   - Handle specific exceptions
   - Provide meaningful error messages

3. **Function Design**
   - Single responsibility principle
   - Clear parameter names
   - Document with docstrings
   - Return meaningful values

4. **Project Structure**
   - Organize code into modules
   - Use virtual environments
   - Maintain requirements.txt
   - Include documentation
