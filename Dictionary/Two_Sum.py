from collections import defaultdict


def two_sum(nums, key):
    num_map = defaultdict(int)  # create an empty dictionary
    for i, num in enumerate(nums):  # here, 'i' is index and 'num' is value at that index of list
        complement = key - num
        if complement in num_map:
            return [num_map[complement], i]  # returns index of complement and ith index
        num_map[num] = i  # key=num, value=i
    return []  # return empty list


if __name__ == "__main__":
    target = int(input("Enter the key"))
    n = input("Enter the number of elements")
    numbers = list(map(int, input("Enter the elements").split()))
    print(two_sum(numbers, target))

'''
Given an array of integers nums and an integer target, return indices of the
two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may
not use the same element twice.
You can return the answer in any order.
'''
