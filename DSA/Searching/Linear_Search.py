def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


if __name__ == "__main__":
    nums = list(map(int, input("Enter the elements of the array").split()))
    key = int(input("Enter the key to be searched"))
    print(linear_search(nums, key))

"""
Linear search is the simplest search algorithm. It checks every element in the list sequentially until the 
desired element is found or the list ends.
"""
