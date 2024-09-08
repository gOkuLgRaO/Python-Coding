def find_peak_element(nums):
    left, right = 0, len(nums) - 1

    while left < right:
        mid = (left + right) // 2
        if nums[mid] < nums[mid + 1]:
            left = mid + 1
        else:
            right = mid
    return left


print(find_peak_element([1, 2, 3, 1]))

"""
A peak element is an element that is strictly greater than its neighbors. Given an integer array nums, find a peak element and return its index.
We use a binary search to find the peak by checking the middle element and adjusting the search range based on the slope.
"""
