"""
Homework 3: Data Structures and File Operations

Instructions:
1. Complete each function according to the requirements
2. Use appropriate data structures (lists, dictionaries, sets)
3. Implement file reading/writing where specified
4. Test your code with the provided test cases
"""

# Task 1: Contact Manager 
def manage_contacts():
    """
    Create a simple contact manager that supports:
    - Adding a contact (name, phone, email)
    - Finding a contact by name
    - Listing all contacts
    - Removing a contact
    
    Store contacts in a dictionary and return it
    """
    contacts = {}
    while True:
        print("\n1. Add Contact")
        print("2. Find Contact")
        print("3. List Contacts")
        print("4. Remove Contact")
        print("5. Exit")
        
        choice = input("Enter choice (1-5): ")
        # Implement the menu options
        # Your code here
        
        if choice == '5':
            break
    
    return contacts

# Task 2: Word Frequency Counter 
def count_word_frequency(filename):
    """
    Read a text file and count word frequencies.
    Return a dictionary with:
    - Word as key (converted to lowercase)
    - Frequency as value
    Handle file not found errors appropriately
    """
    # Your code here
   

# Task 3: Shopping List Manager 
def shopping_list_manager():
    """
    Create a shopping list manager that:
    - Adds items with quantities
    - Removes items
    - Updates quantities
    - Saves list to file 'shopping_list.txt'
    - Loads list from file
    
    Return the current shopping list dictionary
    """
    # Your code here
   

# Test cases
def test_homework():
    # Test Task 1
    contacts = manage_contacts()
    print("Contacts:", contacts)
    
    # Test Task 2
    word_freq = count_word_frequency("sample.txt")
    print("Word Frequencies:", word_freq)
    
    # Test Task 3
    shopping_list = shopping_list_manager()
    print("Shopping List:", shopping_list)

if __name__ == "__name__":
    test_homework()