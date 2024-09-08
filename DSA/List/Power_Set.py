def subsets(nums):
    result = []

    def backtrack(start, path):
        result.append(path)
        for i in range(start, len(nums)):
            backtrack(i + 1, path + [nums[i]])

    backtrack(0, [])
    return result


print(subsets([1, 2, 3]))


"""
Given an integer array nums, return all possible subsets (the power set).
We use backtracking to generate all subsets by either including or excluding each element.
"""
