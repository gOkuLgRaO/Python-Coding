class Solution:
    @staticmethod
    def str_str(haystack: str, needle: str) -> int:
        if len(haystack) < len(needle):
            return -1

        for i in range(len(haystack)):
            if haystack[i : i + len(needle)] == needle:
                return i
        return -1


if __name__ == "__main__":
    strs1 = str(input("Enter the string"))
    strs2 = str(input("Enter the word to search within the string"))
    print(Solution.str_str(strs1, strs2))

"""
Find the position of the first occurrence of the word in the given string
"""
