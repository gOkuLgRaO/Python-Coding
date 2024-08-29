def sum_of_digits(n):
    if n < 0:
        return sum_of_digits(-n)
    if n == 0:
        return 0
    val = n % 10 + sum_of_digits(n // 10)
    return val


if __name__ == "__main__":
    number = int(input("Enter the number"))
    print(sum_of_digits(number))

'''
find the sum of all digits in a number
'''