def is_palindrome(a):
    return a == a[::-1]


if __name__ == "__main__":
    s = input("Enter a string: ")
    result = is_palindrome(s)
    print(result)
