class Solution:
    @staticmethod
    def roman_to_int(s: str) -> int:
        translations = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        number = 0
        length = len(s)

        for i in range(length):
            if i < length - 1 and translations[s[i]] < translations[s[i + 1]]:
                number -= translations[s[i]]
            else:
                number += translations[s[i]]

        return number


if __name__ == "__main__":
    v = str(input("Enter the roman number"))
    solution = Solution()
    print(solution.roman_to_int(v))

"""
Convert the roman numbers into Integer numbers
"""
