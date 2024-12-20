fruits = {"apple", "banana", "orange"}
more_fruits = {"grape", "apple", "mango"}

# Set operations

fruits.add("kiwi")            # Add element
fruits.remove("banana")       # Remove element
union = fruits | more_fruits  # Combine sets
common = fruits & more_fruits # Find intersection
diff = fruits - more_fruits   # Find difference
is_in = "apple" in fruits    # Check membership

print(union)
print(common)
print(diff)
print(is_in)