def create_shopping_list():
    return []

def add_item(shopping_list, item):
    shopping_list.append(item)
    print(f"Added {item} to the list")

def remove_item(shopping_list, item):
    if item in shopping_list:
        shopping_list.remove(item)
        print(f"Removed {item} from the list")
    else:
        print(f"{item} not found in the list")

def show_list(shopping_list):
    if not shopping_list:
        print("List is empty")
    else:
        print("\nShopping List:")
        for item in shopping_list:
            print(f"- {item}")

# Example usage
my_list = create_shopping_list()
add_item(my_list, "Apples")
add_item(my_list, "Bread")
add_item(my_list, "Milk")
show_list(my_list)
remove_item(my_list, "Bread")
show_list(my_list)