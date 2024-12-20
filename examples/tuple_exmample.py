def create_point(x, y):
    return (x, y)

def calculate_distance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

def find_midpoint(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    return ((x1 + x2) / 2, (y1 + y2) / 2)

# Example usage
p1 = create_point(0, 0)
p2 = create_point(3, 4)
distance = calculate_distance(p1, p2)
midpoint = find_midpoint(p1, p2)

print(f"Distance between points: {distance}")
print(f"Midpoint: {midpoint}")