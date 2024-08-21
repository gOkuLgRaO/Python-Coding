def prefix(s):
    if not s:
        return ""

    # Sort the list to bring similar strings closer
    s.sort()

    # Take the first and the last string after sorting
    first = s[0]
    last = s[-1]
    i = 0

    # Compare characters of the first and last string
    while i < len(first) and i < len(last) and first[i] == last[i]:
        i += 1

    # The common prefix is the substring of the first string up to the matching index
    return first[:i]


if __name__ == "__main__":
    strs = list(map(str, input("Enter the words").split()))
    print(prefix(strs))


"""
finding the longest common prefix string amongst an array of strings. 
"""
