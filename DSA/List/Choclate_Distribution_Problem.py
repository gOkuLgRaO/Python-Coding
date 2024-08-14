def chocolate(arr, children):
    packets = len(arr)
    # If there are no chocolates or the number of students is zero
    if children == 0 or packets == 0:
        return 0

    # sort the list
    arr.sort()
    if children > packets:
        return -1

    # Initialize minimum difference
    min_diff = float("inf")

    # Find the minimum difference for all possible sub arrays of size m
    for i in range(packets - children + 1):
        diff = arr[i + children - 1] - arr[i]
        min_diff = min(min_diff, diff)

    return min_diff


if __name__ == "__main__":
    nums = list(
        map(int, input("Enter the number of chocolates in each packet").split())
    )
    m = int(input("Enter the number of children"))
    print(chocolate(nums, m))

"""
/*
 * Given an array of N integers where each value represents the number of
 * chocolates in a packet. Each packet can have a variable number of chocolates.
 * There are m students, the task is to distribute chocolate packets such that:
 * 
 * Each student gets one packet.
 * The difference between the number of chocolates in the packet with maximum
 * chocolates and the packet with minimum chocolates given to the students is
 * minimum.
 * 
 * Input : arr[] = {7, 3, 2, 4, 9, 12, 56} , m = 3
 * Output: Minimum Difference is 2
 * Explanation:
 * We have seven packets of chocolates and we need to pick three packets for 3
 * students
 * If we pick 2, 3 and 4, we get the minimum difference between maximum and
 * minimum packet sizes.
 * 
 * Input : arr[] = {3, 4, 1, 9, 56, 7, 9, 12} , m = 5
 * Output: Minimum Difference is 6
 */
"""
