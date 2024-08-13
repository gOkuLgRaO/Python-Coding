def asc_dsc(arr):
    arr.reverse()
    return arr


if __name__ == "__main__":
    nums = list(map(int, input("Enter the elements").split()))
    nums.sort()
    print(nums)
    print(asc_dsc(nums))

"""
Given a list, sort it and print it in ascending and descending order. 
"""
