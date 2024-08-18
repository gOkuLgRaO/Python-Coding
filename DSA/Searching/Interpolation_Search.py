def interpolation_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high and arr[low] <= target <= arr[high]:
        if low == high:
            if arr[low] == target:
                return low
            return -1

        pos = low + ((target - arr[low]) * (high - low) // (arr[high] - arr[low]))

        if arr[pos] == target:
            return pos
        if arr[pos] < target:
            low = pos + 1
        else:
            high = pos - 1

    return -1


if __name__ == "__main__":
    nums = list(map(int, input("Enter the elements").split()))
    nums.sort()
    key = int(input("Enter the key to be searched"))
    print(interpolation_search(nums, key))
"""
Interpolation search works on uniformly distributed sorted arrays. It estimates the position of the
target using the formula for linear interpolation.
"""
