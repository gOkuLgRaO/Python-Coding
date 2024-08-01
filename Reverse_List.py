def reverse(lst):
    lst.reverse()
    return lst


def reverse_another_method(lst2):
    for i in range(0, len(lst2) // 2):
        temp = lst2[i]
        lst2[i] = lst2[len(lst2) - i - 1]
        lst2[len(lst2) - i - 1] = temp
    return lst2


if __name__ == "__main__":
    nums = list(map(int, input("Enter the list to be reversed").split()))
    print(reverse(nums))
    print(reverse_another_method(nums))

'''
Reverse all the elements of the given list
'''
