import os


def diagonalDifference(arr):
    sum1 = 0
    sum2 = 0

    length = len(arr[0])

    for i in range(length):
        sum1 += arr[i][i]
        sum2 += arr[i][(length - i - 1)]
    return abs(sum1 - sum2)


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + "\n")

    fptr.close()


"""
Given a square matrix, calculate the absolute difference between the sums of its diagonals.
Sample Input

3
11 2 4
4 5 6
10 8 -12
Sample Output

15
Explanation

The primary diagonal is:

11
   5
     -12
Sum across the primary diagonal: 11 + 5 - 12 = 4

The secondary diagonal is:

     4
   5
10
Sum across the secondary diagonal: 4 + 5 + 10 = 19
Difference: |4 - 19| = 15
"""
