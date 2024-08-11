def merge_list(lst1, lst2):
    i = len(lst1) - 1
    j = len(lst2) - 1
    k = len(lst1) + len(lst2) - 1

    lst1.extend([0] * len(lst2))  # Extend lst1 to accommodate elements from lst2
    lst1.extend()
    while j >= 0:
        if i >= 0 and lst1[i] > lst2[j]:
            lst1[k] = lst1[i]
            i -= 1
        else:
            lst1[k] = lst2[j]
            j -= 1

    return lst1


if __name__ == "__main__":
    numbers1 = list(map(int, input("Enter the elements of the first list").split()))
    numbers2 = list(map(int, input("Enter the elements of the second list").split()))
    result = merge_list(numbers1, numbers2)
    print(result)

'''
Merge two sorted lists to form a single list. 
'''