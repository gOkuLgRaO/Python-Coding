class Solution:
    @staticmethod
    def str_str(sentence: str, word: str) -> int:
        if len(sentence) < len(word):
            return -1

        for i in range(len(sentence)):
            if sentence[i : i + len(word)] == word:
                return i
        return -1


if __name__ == "__main__":
    strs1 = str(input("Enter the string"))
    strs2 = str(input("Enter the word to search within the string"))
    print(Solution.str_str(strs1, strs2))

"""
Find the position of the first occurrence of the word in the given string
"""
