from collections import defaultdict


def count_duplicates(lst):
    # create a dictionary to count occurrence of each element
    element_count = defaultdict(int)

    # Traverse the array and count the occurrences of each element
    for ele in lst:
        element_count[ele] += 1

    # Creates a new dictionary duplicates that contains only the elements from element_count which have a count
    # greater than 1
    duplicate = defaultdict(int)
    for ele, counts in element_count.items():  # 'ele' is key and 'count' is value
        if counts > 1:
            duplicate[ele] = counts

    return duplicate


if __name__ == "__main__":
    nums = list(map(int, input("Enter the elements ").split()))
    duplicates = count_duplicates(nums)
    if duplicates:
        for num, count in duplicates.items():  # 'num' is key and 'count' is value
            print(f"Element {num} is duplicated {count} times")
    else:
        print("No duplicates found")

