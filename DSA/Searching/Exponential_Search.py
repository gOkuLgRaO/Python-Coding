def exponential_search(arr, target):
    if arr[0] == target:
        return 0
    n = len(arr)
    i = 1
    while i < n and arr[i] <= target:
        i = i * 2

    return binary_search(arr, i // 2, min(i, n - 1), target)


def binary_search(arr, left, right, target):
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


if __name__ == "__main__":
    nums = list(map(int, input("Enter the elements").split()))
    key = int(input("Enter the target"))
    result = exponential_search(nums, key)
    print(result)
"""
Exponential search is useful when the list is infinite or when the size is unknown. It first finds a range where the
target lies and then applies binary search within that range.
"""
