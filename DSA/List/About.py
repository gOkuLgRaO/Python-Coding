# LIST COMPREHENSION
# -------------------

# Basic List Comprehension:
square = [x**2 for x in range(10)]
print(square)

# List Comprehension with Condition:
even_square = [x**2 for x in range(10) if x % 2 == 0]
print(even_square)

# Nested List Comprehension:
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [num for row in matrix for num in row]


# Using Functions in List Comprehension:
def square(x):
    return x**2


square_func = [square(x) for x in range(5)]
print(square_func)

# List Comprehension with Multiple Conditions:
filtered = [x for x in range(20) if x % 2 == 0 and x % 3 == 0]
