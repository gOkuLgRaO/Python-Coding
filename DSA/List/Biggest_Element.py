def biggest(arr):
    arr.sort()
    return arr[len(arr) - 1]


if __name__ == "__main__":
    nums = list(map(int, input("Enter the elements").split()))
    print(biggest(nums))

"""
return the largest element from the list
"""
