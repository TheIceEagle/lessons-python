# Python Collections and Data Structures - Practice Exercises

## Basic Exercises

### 1. List Manipulation
```python
# Exercise: Create a function that removes duplicates from a list while preserving order
def remove_duplicates(items):
    """
    Remove duplicates from a list while preserving order
    Example:
    >>> remove_duplicates([1, 2, 3, 1, 4, 2, 5])
    [1, 2, 3, 4, 5]
    """
    # Your code here
    pass

# Solution:
def remove_duplicates(items):
    seen = set()
    return [x for x in items if not (x in seen or seen.add(x))]
```

### 2. Dictionary Operations
```python
# Exercise: Create a function that merges two dictionaries and sums values for common keys
def merge_dicts(dict1, dict2):
    """
    Merge two dictionaries, summing values for common keys
    Example:
    >>> merge_dicts({'a': 1, 'b': 2}, {'b': 3, 'c': 4})
    {'a': 1, 'b': 5, 'c': 4}
    """
    # Your code here
    pass

# Solution:
def merge_dicts(dict1, dict2):
    result = dict1.copy()
    for key, value in dict2.items():
        result[key] = result.get(key, 0) + value
    return result
```

## Intermediate Exercises

### 3. Set Operations
```python
# Exercise: Create a function that finds common elements in two lists using sets
def find_common_elements(list1, list2):
    """
    Find common elements between two lists, maintaining order of first list
    Example:
    >>> find_common_elements([1, 2, 3, 4], [3, 4, 5, 6])
    [3, 4]
    """
    # Your code here
    pass

# Solution:
def find_common_elements(list1, list2):
    set2 = set(list2)
    return [x for x in list1 if x in set2]
```

### 4. Nested Data Structures
```python
# Exercise: Create a function that flattens a nested list
def flatten_list(nested_list):
    """
    Flatten a nested list of arbitrary depth
    Example:
    >>> flatten_list([1, [2, 3, [4, 5]], 6])
    [1, 2, 3, 4, 5, 6]
    """
    # Your code here
    pass

# Solution:
def flatten_list(nested_list):
    flat_list = []
    for item in nested_list:
        if isinstance(item, list):
            flat_list.extend(flatten_list(item))
        else:
            flat_list.append(item)
    return flat_list
```

## Advanced Exercises

### 5. Custom Data Structure
```python
# Exercise: Implement a Stack using a list
class Stack:
    """
    Implement a Stack with push, pop, peek, and is_empty operations
    Example:
    >>> stack = Stack()
    >>> stack.push(1)
    >>> stack.push(2)
    >>> stack.peek()
    2
    >>> stack.pop()
    2
    """
    def __init__(self):
        # Your code here
        pass
    
    def push(self, item):
        # Your code here
        pass
    
    def pop(self):
        # Your code here
        pass
    
    def peek(self):
        # Your code here
        pass
    
    def is_empty(self):
        # Your code here
        pass

# Solution:
class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        raise IndexError("Stack is empty")
    
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        raise IndexError("Stack is empty")
    
    def is_empty(self):
        return len(self.items) == 0
```

### 6. Real-World Application
```python
# Exercise: Create a function that implements a frequency-based cache
class FrequencyCache:
    """
    Implement a cache that keeps track of most frequently used items
    Example:
    >>> cache = FrequencyCache(max_size=2)
    >>> cache.add('a', 1)
    >>> cache.add('b', 2)
    >>> cache.add('c', 3)  # Should remove least frequently used item
    >>> cache.get('a')     # Should return None as 'a' was removed
    None
    """
    def __init__(self, max_size):
        # Your code here
        pass
    
    def add(self, key, value):
        # Your code here
        pass
    
    def get(self, key):
        # Your code here
        pass

# Solution:
class FrequencyCache:
    def __init__(self, max_size):
        self.max_size = max_size
        self.cache = {}
        self.frequency = {}
    
    def add(self, key, value):
        if len(self.cache) >= self.max_size:
            # Remove least frequently used item
            min_freq = min(self.frequency.values())
            for k, freq in self.frequency.items():
                if freq == min_freq:
                    del self.cache[k]
                    del self.frequency[k]
                    break
        
        self.cache[key] = value
        self.frequency[key] = 0
    
    def get(self, key):
        if key in self.cache:
            self.frequency[key] += 1
            return self.cache[key]
        return None
```

## Practice Projects

### 1. Contact Manager
```python
"""
Create a contact manager that supports:
- Adding contacts (name, phone, email)
- Removing contacts
- Searching contacts
- Grouping contacts
- Export/Import contacts to/from file
"""

class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

class ContactManager:
    def __init__(self):
        self.contacts = {}
        self.groups = defaultdict(set)
    
    def add_contact(self, name, phone, email):
        """Add a new contact"""
        self.contacts[name] = Contact(name, phone, email)
    
    def remove_contact(self, name):
        """Remove a contact"""
        if name in self.contacts:
            del self.contacts[name]
            for group in self.groups.values():
                group.discard(name)
    
    def search(self, term):
        """Search contacts by name, phone, or email"""
        results = []
        term = term.lower()
        for contact in self.contacts.values():
            if (term in contact.name.lower() or
                term in contact.phone or
                term in contact.email.lower()):
                results.append(contact)
        return results
    
    def add_to_group(self, name, group):
        """Add contact to a group"""
        if name in self.contacts:
            self.groups[group].add(name)
    
    def export_contacts(self, filename):
        """Export contacts to JSON file"""
        with open(filename, 'w') as f:
            data = {
                'contacts': {
                    name: {
                        'phone': contact.phone,
                        'email': contact.email
                    }
                    for name, contact in self.contacts.items()
                },
                'groups': {
                    group: list(members)
                    for group, members in self.groups.items()
                }
            }
            json.dump(data, f, indent=2)
```

### 2. Data Analysis Tool
```python
"""
Create a tool for analyzing data that supports:
- Loading data from different sources
- Computing statistics
- Filtering data
- Grouping and aggregating data
- Exporting results
"""

class DataAnalyzer:
    def __init__(self):
        self.data = []
        self.columns = []
    
    def load_csv(self, filename):
        """Load data from CSV file"""
        with open(filename, 'r') as f:
            reader = csv.reader(f)
            self.columns = next(reader)
            self.data = [row for row in reader]
    
    def filter_data(self, column, condition):
        """Filter data based on condition"""
        col_idx = self.columns.index(column)
        return [row for row in self.data if condition(row[col_idx])]
    
    def group_by(self, column):
        """Group data by column"""
        col_idx = self.columns.index(column)
        groups = defaultdict(list)
        for row in self.data:
            groups[row[col_idx]].append(row)
        return dict(groups)
    
    def aggregate(self, column, func):
        """Compute aggregate statistics"""
        col_idx = self.columns.index(column)
        values = [float(row[col_idx]) for row in self.data]
        return func(values)
```

