def remove_element(lst, k):
    j = 0
    for i in range(len(lst)):
        if lst[i] != k:
            lst[j] = lst[i]
            j += 1
    return lst[:j]


if __name__ == "__main__":
    key = int(input("Enter the element which needs to be removed"))
    numbers = list(map(int, input("Enter the elements of the list").split()))
    res = remove_element(numbers, key)
    print(res)

'''
The key which user tells needs to be removed from the list. 
'''