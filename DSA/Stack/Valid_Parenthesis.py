class Solution(object):
    @staticmethod
    def is_valid(s):
        stack = []  # create an empty stack to store opening brackets.
        for c in s:
            if c in "([{":
                stack.append(c)
            else:
                if (
                    not stack
                    or (c == ")" and stack[-1] != "(")
                    or (c == "}" and stack[-1] != "{")
                    or (c == "]" and stack[-1] != "[")
                ):
                    return False
                stack.pop()
        return (
            not stack
        )  # if the stack is empty, all opening brackets have been matched with their corresponding
        # closing brackets, so the string is valid, otherwise, there are unmatched opening brackets, so return false


if __name__ == "__main__":
    strs = list(map(str, input("Enter the string")))
    print(Solution.is_valid(strs))


"""
check if the parenthesis are correctly closed in the string. 
"""
