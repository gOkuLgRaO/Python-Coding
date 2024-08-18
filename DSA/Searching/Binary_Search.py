def binary_search(arr, target):
    left, right = 0, len(arr) - 1
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
    key = int(input("Enter the element to search"))
    nums.sort()
    print(binary_search(nums, key))

"""
Binary search is an efficient algorithm that works on sorted arrays. It repeatedly divides the search 
interval in half, reducing the search space significantly.
"""
