def increments(n):
    if n < 0:
        return
    print(n)
    increments(n - 1)


def increments_reverse(n):
    if n < 0:
        return
    increments_reverse(n - 1)
    print(n)


if __name__ == "__main__":
    val = int(input("Enter the number"))
    print(increments(val))
    print(increments_reverse(val))

'''
This explains about stack memory of local variables within a function. 
'''