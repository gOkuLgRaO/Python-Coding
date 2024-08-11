def search(nums, key):
    try:
        index = nums.index(key)
        return index, True
    except ValueError:
        return False


if __name__ == "__main__":
    element = int(input("Enter the key to be searched"))
    numbers = list(map(int, input("Enter the elements of the list").split()))
    print(search(numbers, element))

'''
check if the element is present in the list
'''
