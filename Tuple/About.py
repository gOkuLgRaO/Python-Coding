"""
A tuple is immutable(cannot change) sequence of python objects
Tuples are also comparable and hashable

We generally use List for homogenous(same) data types.
We use tuples for heterogeneous (different) data types.
As tuples are immutable, they can be used as keys for the dictionaries.
"""

newTuple = 'a', 'b', 'c', 'd', 'e'  # These are the different elements of the tuple.
newTuple_num = (1, 2, 3, 4, 5, 6)
newTuple_num2 = (4, 5, 6, 7, 8, 9)
newTuple2 = ('a',)  # the comma is necessary when you have only one element in the tuple
newTuple3 = tuple('abcde')  # even character will be treated as element of the tuple.

print(newTuple[1])  # You can access the element via its index position in the tuple.
print(newTuple[-1])  # To access the last element
print(newTuple[-2])  # last but one element.
print(newTuple[1: 3])  # index 3 is not included in the slicing.
print(newTuple[: 3])  # started from 0th index till 2nd index position.
print(newTuple[:])  # prints all elements
for i in newTuple:
    print(i)  # traversing the tuple

for i in range(len(newTuple)):  # another way of traversal
    print(newTuple[i])

print('b' in newTuple)  # This expression returns true or false.


def search_tuple(p_tuple, element):  # searching for index position of the element in the tuple.
    for ele in p_tuple:
        if ele == element:
            return p_tuple.index(ele)
    return 'The element does not exist in the tuple'


list1 = [(1, 2), (9, 0)]
sample_tuple = ((1, 2), (9, 0))
print(list1)
print(sample_tuple)

print(newTuple_num + newTuple_num2)  # concatenate two tuples
print(newTuple_num * 4)  # elements of the tuple will be repeated 4 times.
print(newTuple_num.count(2))  # counts how many times element '2' has been emerged in the tuple.
print(max(newTuple_num))  # returns the maximum element
print(min(newTuple_num))  # returns the minimum element
print(tuple([1, 2, 3, 4]))  # converts the list into tuple.
print(search_tuple(newTuple, 'c'))
print(newTuple)
print(newTuple2)
print(newTuple3)

# Time complexity: O(1)
# space complexity: O(n)
