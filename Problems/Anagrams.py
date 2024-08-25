from collections import Counter


def anagrams(str1, str2):
    return Counter(str1) == Counter(str2)


if __name__ == "__main__":
    print("Enter the two string")
    a = str(input("Enter the first string"))
    b = str(input("Enter the second string"))
    print(anagrams(a, b))


"""
check the number of occurrence of each letter of two words, if they are same. 
"""
