# while loop
#
# while 1 == 1:
#     print("I am in a loop")

name = input("Enter your name: ")

while name == "":
    name = input("Enter your name: ")

age = int(input("What is your age?: "))

while age < 0:
    print("Age cant be less than 0")
    age = int(input("What is your age?: "))

print(f"Hello {name}")
print(f"You are {age} years old")