def count_subarray(arr):
    n = len(arr)
    count = 0
    for i in range(n):
        res = 0
        for j in range(i, n):
            res += arr[j]
            if res < 0:
                count += 1
    return count


if __name__ == "__main__":
    nums = list(map(int, input("Enter the elements of the array").split()))
    print(count_subarray(nums))

"""
Count the number of sub arrays whose values are negative. 
"""
