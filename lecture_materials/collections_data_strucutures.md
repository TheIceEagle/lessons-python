# Python Collections and Data Structures - Comprehensive Guide

## Table of Contents
1. [Lists](#lists)
2. [Tuples](#tuples)
3. [Dictionaries](#dictionaries)
4. [Sets](#sets)
5. [Advanced Operations](#advanced-operations)
6. [Performance Considerations](#performance-considerations)
7. [Common Use Cases](#common-use-cases)

## Lists

Lists are mutable, ordered sequences that can store any type of object.

### Creating Lists
```python
# Empty list
empty_list = []
empty_list = list()

# List with items
numbers = [1, 2, 3, 4, 5]
mixed = [1, "hello", 3.14, True, [1, 2]]
```

### List Operations
```python
# Accessing elements
numbers = [1, 2, 3, 4, 5]
first = numbers[0]      # => 1
last = numbers[-1]      # => 5

# Slicing
first_three = numbers[0:3]    # => [1, 2, 3]
skip_step = numbers[::2]      # => [1, 3, 5]
reversed = numbers[::-1]      # => [5, 4, 3, 2, 1]

# Modifying lists
numbers.append(6)       # Add to end: [1, 2, 3, 4, 5, 6]
numbers.insert(0, 0)   # Add at index: [0, 1, 2, 3, 4, 5, 6]
numbers.extend([7, 8]) # Add multiple: [0, 1, 2, 3, 4, 5, 6, 7, 8]
numbers.pop()          # Remove & return last: 8
numbers.pop(0)         # Remove & return index: 0
numbers.remove(5)      # Remove first occurrence of value
numbers.clear()        # Remove all items

# Finding elements
numbers = [1, 2, 3, 2, 4]
count_2 = numbers.count(2)    # => 2 (counts occurrences)
index_2 = numbers.index(2)    # => 1 (first occurrence)

# Sorting
numbers.sort()                # Sort in place
numbers.sort(reverse=True)    # Sort in descending order
sorted_numbers = sorted(numbers)  # Return new sorted list
```

### List Comprehensions
```python
# Basic comprehension
squares = [x**2 for x in range(5)]  # => [0, 1, 4, 9, 16]

# Comprehension with condition
evens = [x for x in range(10) if x % 2 == 0]  # => [0, 2, 4, 6, 8]

# Nested comprehension
matrix = [[i+j for j in range(3)] for i in range(3)]
# => [[0, 1, 2],
#     [1, 2, 3],
#     [2, 3, 4]]
```

## Tuples

Tuples are immutable, ordered sequences. They're like lists that can't be changed after creation.

### Creating Tuples
```python
# Empty tuple
empty_tuple = ()
empty_tuple = tuple()

# Single item tuple (note the comma)
single = (1,)

# Multiple items
coordinates = (10, 20)
mixed = (1, "hello", 3.14)
```

### Tuple Operations
```python
# Unpacking
x, y = coordinates        # x = 10, y = 20
first, *rest = (1, 2, 3, 4)  # first = 1, rest = [2, 3, 4]

# Concatenation
combined = (1, 2) + (3, 4)  # => (1, 2, 3, 4)

# Methods
coords = (10, 20, 30, 20)
coords.count(20)    # => 2
coords.index(30)    # => 2
```

## Dictionaries

Dictionaries are mutable, unordered collections of key-value pairs.

### Creating Dictionaries
```python
# Empty dictionary
empty_dict = {}
empty_dict = dict()

# Dictionary with items
person = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

# Alternative creation methods
dict_from_tuples = dict([("a", 1), ("b", 2)])
dict_from_kwargs = dict(name="John", age=30)
```

### Dictionary Operations
```python
# Accessing values
name = person["name"]          # Using key
age = person.get("age", 25)    # With default value

# Modifying dictionaries
person["email"] = "john@example.com"  # Add new key-value
person.update({"phone": "123-456"})   # Add multiple
del person["age"]                     # Remove key-value
removed = person.pop("email")         # Remove and return
person.clear()                        # Remove all items

# Dictionary methods
keys = list(person.keys())          # Get all keys
values = list(person.values())      # Get all values
items = list(person.items())        # Get all key-value pairs

# Dictionary comprehension
squares = {x: x**2 for x in range(5)}
# => {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
```

## Sets

Sets are mutable, unordered collections of unique elements.

### Creating Sets
```python
# Empty set (can't use {})
empty_set = set()

# Set with items
numbers = {1, 2, 3, 4, 5}
unique = {1, 2, 2, 3, 3, 4}  # => {1, 2, 3, 4}
```

### Set Operations
```python
# Adding and removing
numbers.add(6)          # Add single item
numbers.update([7, 8])  # Add multiple items
numbers.remove(6)       # Remove item (raises error if not found)
numbers.discard(6)      # Remove item (no error if not found)
numbers.pop()           # Remove and return arbitrary item
numbers.clear()         # Remove all items

# Set operations
set1 = {1, 2, 3}
set2 = {3, 4, 5}

# Union (all unique elements from both sets)
union = set1 | set2               # => {1, 2, 3, 4, 5}
union = set1.union(set2)          # Same as above

# Intersection (elements present in both sets)
intersection = set1 & set2        # => {3}
intersection = set1.intersection(set2)

# Difference (elements in set1 but not in set2)
difference = set1 - set2          # => {1, 2}
difference = set1.difference(set2)

# Symmetric difference (elements in either set but not both)
sym_diff = set1 ^ set2           # => {1, 2, 4, 5}
sym_diff = set1.symmetric_difference(set2)

# Subset and superset
{1, 2}.issubset({1, 2, 3})       # => True
{1, 2, 3}.issuperset({1, 2})     # => True
```

## Advanced Operations

### Nested Data Structures
```python
# Complex data structure
data = {
    "users": [
        {
            "id": 1,
            "name": "John",
            "roles": {"admin", "user"}
        },
        {
            "id": 2,
            "name": "Jane",
            "roles": {"user"}
        }
    ],
    "active": True
}

# Accessing nested elements
first_user_name = data["users"][0]["name"]
first_user_roles = data["users"][0]["roles"]
```

### Common Patterns
```python
# Defaultdict for automatic default values
from collections import defaultdict
counts = defaultdict(int)
words = ["apple", "banana", "apple", "cherry"]
for word in words:
    counts[word] += 1  # No KeyError if word doesn't exist

# Counter for counting elements
from collections import Counter
word_counts = Counter(words)
print(word_counts)  # Counter({'apple': 2, 'banana': 1, 'cherry': 1})

# Named tuples for readable code
from collections import namedtuple
Point = namedtuple('Point', ['x', 'y'])
p = Point(11, 22)
print(p.x, p.y)  # 11 22
```

## Performance Considerations

1. **Lists vs. Tuples**
   - Tuples are more memory efficient
   - Tuples are slightly faster for lookup
   - Use lists when you need to modify contents
   - Use tuples for fixed data

2. **Dictionaries and Sets**
   - O(1) average case for lookups
   - Use sets for membership testing
   - Dictionaries preserve insertion order (Python 3.7+)
   - Sets use less memory than dictionaries

3. **List Operations**
   - append() is O(1)
   - insert() is O(n)
   - in operator is O(n)
   - Sorting is O(n log n)

## Common Use Cases

1. **Lists**
   - Ordered sequences of items
   - Task queues
   - Stack implementation
   - Historical data

2. **Tuples**
   - Return values from functions
   - Dictionary keys (when needed)
   - Data that shouldn't change
   - Coordinates or points

3. **Dictionaries**
   - Key-value mappings
   - Caching/memoization
   - Frequency counting
   - Object properties

4. **Sets**
   - Removing duplicates
   - Membership testing
   - Mathematical set operations
   - Unique constraints

## Practical Examples

```python
# Example 1: Frequency Counter
def word_frequency(text):
    words = text.lower().split()
    return Counter(words)

# Example 2: Unique Items
def get_unique_emails(users):
    return {user['email'] for user in users}

# Example 3: Data Transformation
def users_by_country(users):
    result = defaultdict(list)
    for user in users:
        result[user['country']].append(user['name'])
    return dict(result)

# Example 4: Cache Implementation
def memoize(func):
    cache = {}
    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrapper
```

