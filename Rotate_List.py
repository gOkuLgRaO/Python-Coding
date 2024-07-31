def rotate(nums, index):
    reverse(nums, 0, len(nums) - 1)
    reverse(nums, 0, index - 1)
    reverse(nums, index, len(nums) - 1)
    return nums


def reverse(number, start, end):
    while start < end:
        swap(number, start, end)
        start += 1
        end += 1


def swap(num, i, j):
    temp = num[i]
    num[i] = num[j]
    num[j] = temp


if __name__ == "__main__":
    position = int(input("Enter the position from where it has to be reversed"))
    input_list = list(map(int, input("Enter the elements of the list").split()))
    print(rotate(input_list, position))

'''
rotate the given list according to index given by the user
Example 1:
 * 
 * Input: nums = [1,2,3,4,5,6,7], k = 3
 * Output: [5,6,7,1,2,3,4]
 * Explanation:
 * rotate 1 steps to the right: [7,1,2,3,4,5,6]
 * rotate 2 steps to the right: [6,7,1,2,3,4,5]
 * rotate 3 steps to the right: [5,6,7,1,2,3,4]
 '''