# Basic Dictionary Comprehension
# create a dictionary where keys are numbers and values are their squares
squares = {x: x ** 2 for x in range(6)}
print(squares)

# Using Conditionals in Dictionary Comprehensions
# Create a dictionary with only even numbers and their squares.
even = {x: x ** 2 for x in range(6) if x % 2 == 0}
print(even)

# Using Nested Loops in Dictionary Comprehensions
# Create a dictionary from two lists using a nested loop.
keys = ['a', 'b', 'c']
values = [1, 2, 3]
combine = {k: v for k in keys for v in values}
print(combine)

# Nested Dictionary Comprehension
# Create a nested dictionary where the keys are numbers, and the values are dictionaries with numbers
# as keys and their cubes as values.
nested_dict = {x: {y: y ** 3 for y in range(x)} for x in range(6)}
print(nested_dict)

# Using a Function in Dictionary Comprehensions
# Create a dictionary with keys as strings and values as the length of those strings.
words = ['apple', 'samsung', 'nokia', 'OnePlus']
func_dict = {word: len(word) for word in words}
print(func_dict)

# Merging Two Lists into a Dictionary
# Create a dictionary by merging two lists, one for keys and one for values.
keys2 = ['a', 'b', 'c']
values2 = [1, 2, 3]
combine2 = {k: v for k, v in zip(keys2, values2)}
print(combine2)

# Swapping Keys and Values
# Create a dictionary by swapping the keys and values of an existing dictionary.
original = {'a': 1, 'b': 2, 'c': 3}
swapped = {k: v for v, k in original.values()}

# Combining Multiple Dictionaries
# Combine multiple dictionaries into one.
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
combined_dict = {k: v for d in [dict1, dict2] for k, v in d.items()}

# Conditional Dictionary Comprehension with Multiple Conditions
# Create a dictionary with keys as numbers and values as 'even' or 'odd' based on the condition.
even_odd = {k: 'even' if k % 2 == 0 else 'odd' for k in range(6)}
