import math


def power(n):
    if n == 1:
        return True
    elif n <= 0:
        return False
    else:
        log_four = math.log(n) / math.log(4)
        return log_four == int(log_four)


if __name__ == "__main__":
    nums = int(input("Enter the number"))
    print(power(nums))

"""
check if the number is power of 4 or not
"""
