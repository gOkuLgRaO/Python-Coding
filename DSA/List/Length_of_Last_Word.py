class Solution:
    @staticmethod
    def length_of_last_word(s: str) -> int:
        length = 0
        counting = False

        for c in s:
            if c != " ":
                if not counting:
                    counting = True
                    length = 1
                else:
                    length += 1
            else:
                counting = False

        return length


if __name__ == "__main__":
    strs = str(input("Enter the string"))
    print(Solution.length_of_last_word(strs))
