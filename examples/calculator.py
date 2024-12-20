def add_numbers(a, b):
    return a + b

def calculate_average(numbers):
    return sum(numbers) / len(numbers)

def calculate_grade():
    grades = []
    while True:
        grade = input("Enter grade (or 'done' to finish): ")
        if grade.lower() == 'done':
            break
        grades.append(float(grade))
    
    
    average = calculate_average(grades)
    highest = max(grades)
    lowest = min(grades)
    
    print(f"Average: {average:.2f}")
    print(f"Highest: {highest}")
    print(f"Lowest: {lowest}")


# result = add_numbers(5, 3)
# print(f"5 + 3 = {result}")

if __name__ == "__main__":
    calculate_grade()