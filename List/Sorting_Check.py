def sorting_check(nums, n):
    if n == len(nums) - 1:
        return True
    return nums[n] < nums[n + 1] and sorting_check(nums, n + 1)


if __name__ == "__main__":
    number = list(map(int, input("Enter the number").split()))
    print(sorting_check(number, 0))

'''
check if the elements within a list are sorted
'''