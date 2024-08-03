def pivot(lst):
    res = 0
    for i in range(len(lst)):
        res += lst[i]
    left = 0
    for i in range(len(lst)):
        if left * 2 + lst[i] == res:
            return i
        left += lst[i]


if __name__ == "__main__":
    numbers = list(map(int, input("Enter the elements of the list").split()))
    print(pivot(numbers))

'''
Pivot element is the element for which the sum of elements in left side is equal 
to the elements of the right
'''