def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)


if __name__ == "__main__":
    nums = int(input("Enter the number"))
    print(factorial(nums))

"""
To find the factorial of a number. 
"""
