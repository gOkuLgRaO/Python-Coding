def count_zeroes(nums, count):
    if nums == 0:
        return False
    if nums % 10 == 0:
        count_zeroes(nums // 10, count + 1)
    return count_zeroes(nums // 10, count)


if __name__ == "__main__":
    n = int(input("Enter the number"))
    count_zeroes(n, 0)

'''
count the number of zeroes in a given number 
'''