


# List[] is a collection which is ordered and changeable. Allows duplicate members.
# Tuple() is a collection which is ordered and unchangeable. Allows duplicate members.
# Set{} is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
# Dictionary is a collection which is ordered** and changeable. No duplicate members.

# fruits = ["apple","orange","pineapple","watermelon"]

# # fruits[3] = "banana"
# fruits.append("mango")
# fruits.remove("orange")
# fruits.pop(1)
# fruits.clear()

# print(fruits)
#
# # # iterate and print all elements
# for fruit in fruits:
#     print(fruit, end=" ")


"""Tuple""" 
# Collection which cant be changed

fruits = ("kiwi","apple","orange","pineapple","watermelon")
# cant change element, will give an error
# fruits[0] = "mango"
# trying to append will not work


# print(fruits[2])

# """Sets"""
#
#
fruits = {"kiwi","apple","orange","pineapple","watermelon"}

# doesnt support indexing
# fruits[0] = "banana"

# can add/remove from set

# fruits.add("banana")
print(fruits)
fruits.remove("apple")
duplicates = {1, 2, 3} | {2, 3, 4}

# fruits.clear()
print(duplicates)
