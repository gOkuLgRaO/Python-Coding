def remove_duplicates(nums):
    if not nums:  # if there are no elements
        return 0

    j = 1  # because 0th element is always unique
    for i in range(1, len(nums)):
        if nums[i] != nums[i - 1]:
            nums[j] = nums[i]
            j += 1
    return nums[:j]


if __name__ == "__main__":
    numbers = list(map(int, input("Enter the numbers in increasing order ").split()))
    result = remove_duplicates(numbers)
    print(result)

'''
Given an integer array nums sorted in non-decreasing order, remove the
duplicates in-place such that each unique element appears only once. The
relative order of the elements should be kept the same. Then return the
number of unique elements in nums.
'''