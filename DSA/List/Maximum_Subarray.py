def subarray(arr):
    current_sum = 0
    max_sum = 0

    for i in range(1, len(arr)):
        current_sum = max(arr[i], current_sum + arr[i])
        max_sum = max(max_sum, current_sum)

    return max_sum


if __name__ == "__main__":
    nums = list(map(int, input("Enter the elements").split()))
    print(subarray(nums))

"""
Find the sub array which gives the maximum value upon adding
"""
