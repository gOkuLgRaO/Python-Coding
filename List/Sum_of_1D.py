def sum1d(lst):
    res = 0
    for i in range(0, len(lst)):
        res += lst[i]
    return res


if __name__ == "__main__":
    numbers = list(map(int, input("Enter the elements of the list").split()))
    result = sum1d(numbers)
    print(result)

'''
sum of all the elements of the list. 
'''