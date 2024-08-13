def majority(n):
    return n[int(len(n) / 2)]


if __name__ == "__main__":
    nums = list(map(int, input("Enter the elements").split()))
    print(majority(nums))


"""
return the element which occurs most of the times. 
"""
