def armstrong(n):
    original = n
    last = 0
    while n > 0:
        last += (n % 10) ** 3
        n //= 10
    return last == original


if __name__ == "__main__":
    num = int(input("Enter the number"))
    print(armstrong(num))

'''
his function checks if a given number n is an Armstrong number by calculating the sum of the cubes of 
its digits and comparing it to the original number.
'''