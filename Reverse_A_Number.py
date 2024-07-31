def reverse(n):
    result = 0
    while n > 0:
        val = n % 10
        result = result * 10 + val
        n = n // 10
    return result


if __name__ == "__main__":
    number = int(input("Enter the number to be reversed"))
    print(reverse(number))

'''
Reverse a given number by the user
'''
