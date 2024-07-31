def leap_year(n):
    if not n:
        return 0

    if n % 400 == 0:
        return False
    elif n % 4 == 0 and n % 100 != 0:
        return True

    return False


if __name__ == "__main__":
    year = int(input("Enter the year"))
    print(leap_year(year))

'''
check if the year is leap year or not
'''