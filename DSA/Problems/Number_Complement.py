class Solution:
    @staticmethod
    def find_complement(num: int) -> int:
        bit_length = (
            num.bit_length()
        )  # find the bit length of the binary number entered
        mask = (1 << bit_length) - 1
        # Here, 1 << bit_length is a bitwise left shift of 1 by bit_length bits. This creates a number where the
        # leftmost bit is 1, followed by bit_length number of 0s.
        # Subtracting 1 from this value gives a number where all bits in the bit_length are set to 1.
        # Example:
        # If bit_length = 3, then 1 << 3 gives 1000 in binary (which is 8 in decimal).
        # Subtracting 1 gives 0111 in binary (which is 7 in decimal).
        # So, the mask is 7.
        return num ^ mask


if __name__ == "__main__":
    nums = int(input("Enter the binary number"))
    print(Solution.find_complement(nums))


"""
find the complement of the binary number entered. 
"""
