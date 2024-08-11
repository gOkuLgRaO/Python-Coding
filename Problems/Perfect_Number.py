def perfect(n):
    if n < 2:
        return False
    res = 1
    for i in range(2, int(n // 2) + 1):
        if n % i == 0:
            res += i
            if i != n // i:
                res += n // i

    return res == n


if __name__ == "__main__":
    number = int(input("Enter the number"))
    print(perfect(number))
'''
A perfect number is a positive integer that is equal to the sum of its proper divisors (excluding itself).
'''
