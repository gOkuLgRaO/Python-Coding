from collections import defaultdict
"""
Create a dictionary representing a phone book. Add a few contacts, update a contact,
delete a contact, and retrieve a contact.
"""
# noinspection PyDictCreation
phone_book = {"Alice": "000-111-2222", "Bob": "987-654-3210", "Charlie": "555-555-5555"}

# add a new contact
phone_book["David"] = "111-222-3333"

# update a contact's phone number
phone_book["Alice"] = "000-111-2222"

# delete a contact
del phone_book["Charlie"]

# Retrieve a contact's phone number
alice_number = phone_book.get("Alice")
print(f"Alice's number: {alice_number}")

# Output the updated phone book
print(phone_book)

"""
Create a dictionary of students and their grades. Iterate through the dictionary to print each student's name and grade.
"""

grades = {"Alice": 90,
          "Bob": 85,
          "Charlie": 92,
          "David": 88
          }
for student, grade in grades:
    print(f"{student} got {grade}")

"""
Given a list of words, create a dictionary where the keys are the words and the values are the lengths of the words.
"""

words = ["apple", "banana", "cherry", "date"]

# Dictionary comprehension to create a dictionary with word lengths
word_length = {word: len(word) for word in words}
print(word_length)

"""
Merge two dictionaries into one.
"""

dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}

# merge dictionaries
merged_dict = {**dict1, **dict2}

"""
Create a nested dictionary to represent the information of employees in a company. The keys are employee IDs, 
and the values are dictionaries containing the employee's name, age, and department.
"""

employees = {
    1001: {"name": "Alice", "age": 30, "department": "HR"},
    1002: {"name": "Bob", "age": 25, "department": "Engineering"},
    1003: {"name": "Charlie", "age": 28, "department": "Marketing"}
}

# access info about the employee
employee_id = 1002
employee_info = employees.get(employee_id, "Employee not found")
print(employee_info)

"""
Given a dictionary, demonstrate the use of the keys(), values(), and items() methods.
"""
# Dictionary
sample_dict = {"a": 1, "b": 2, "c": 3}

# get all keys
keys = sample_dict.keys()
print(f"Keys: {list(keys)}")

# Get all values
values = sample_dict.values()
print(f"Values: {list(values)}")

# Get all key-value pairs
items = sample_dict.items()
print(f"Items: {list(items)}")

"""
Given a list of integers, count the frequency of each element using a dictionary.
"""
# List of integers
numbers = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]

# dictionary to count frequency
frequency = {}
for number in numbers:
    if number in frequency:
        frequency[number] += 1
    else:
        frequency[number] = 1

print(frequency)

"""
Use defaultdict from the collections module to count the frequency of elements in a list.
"""


# List of integers
numbers = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]

# Default dictionary to count frequency
frequency = defaultdict(int)

for number in numbers:
    frequency[number] += 1

print(dict(frequency))

# DICTIONARY COMPREHENSION
# ----------------------------

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
