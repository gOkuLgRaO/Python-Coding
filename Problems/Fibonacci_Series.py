def fibonacci(n):
    fib = [0] * n
    fib[0] = 0
    fib[1] = 1
    for i in range(2, n):
        fib[i] = fib[i - 1] + fib[i - 2]
    return fib


if __name__ == "__main__":
    number = int(input("Enter the length of the fibonacci you want"))
    print(fibonacci(number))

'''
find the fibonacci series for length of 'n'
'''