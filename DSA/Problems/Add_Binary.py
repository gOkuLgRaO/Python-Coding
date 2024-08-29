class Solution:
    @staticmethod
    def add_binary(a, b):
        a = int(a, 2)  # converts the binary string into integer value
        b = int(b, 2)
        res = a + b
        return bin(res)[2:]  # returning from the second place by neglecting "0b"


if __name__ == "__main__":
    strs1 = str(input("Enter the first binary number"))
    strs2 = str(input("Enter the second binary number"))
    print(Solution.add_binary(strs1, strs2))


"""
To return the sum of two binary numbers. 
"""
