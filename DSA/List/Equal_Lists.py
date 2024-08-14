def compare(arr1, arr2):
    if arr1 == arr2:
        return True
    return False


if __name__ == "__main__":
    nums1 = list(map(int, input("Enter the elements of the first list").split()))
    nums2 = list(map(int, input("Enter the elements of the second list").split()))
    print(compare(nums1, nums2))

"""
Check if the two lists are equal or not. 
"""
