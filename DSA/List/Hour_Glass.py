def hour_glass(arr):
    max_sum = float("-inf")

    for i in range(4):
        for j in range(4):
            current_sum = (
                arr[i][j]
                + arr[i][j + 1]
                + arr[i][j + 2]
                + arr[i + 1][j + 1]
                + arr[i + 2][j]
                + arr[i + 2][j + 1]
                + arr[i + 2][j + 2]
            )
            if current_sum > max_sum:
                max_sum = current_sum
    return max_sum


if __name__ == "__main__":
    matrix = []
    print("Enter the elements of the 6x6 array row by row:")
    for i in range(6):
        matrix.append(list(map(int, input().split())))
    result = hour_glass(matrix)
    print(result)


"""
* You are given a 6*6 2D array. An hourglass in an array is a portion shaped
 * like this:
 * a b c
 * d
 * e f g
 * if we create an hourglass using the number 1 within an array full of zeros,
 * it may look like this:
 * 1 1 1 0 0 0
 * 0 1 0 0 0 0
 * 1 1 1 0 0 0
 * 0 0 0 0 0 0
 * 0 0 0 0 0 0
 * 0 0 0 0 0 0
 * Actually, there are many hourglasses in the array above. The three leftmost
 * hourglasses are the following:
 * 1 1 1 1 1 0 1 0 0
 * 1 0 0
 * 1 1 1 1 1 0 1 0 0
 * The sum of an hourglass is the sum of all the numbers within it. The sum for
 * the hourglasses
 * above are 7, 4, and 2, respectively.
 *
 * In this problem you have to print the largest sum among all the hourglasses
 * in the array.
"""
