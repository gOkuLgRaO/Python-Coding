def hcf(num1, num2):
    n = 1
    if num1 != num2:
        while n != 0:
            n = num1 % num2
            if n != 0:
                num1 = num2
                num2 = n

    return num2


if __name__ == "__main__":
    n1 = int(input("Enter the first number"))
    n2 = int(input("Enter the second number"))
    print(hcf(n1, n2))

'''
find the HCF of two numbers. 
'''