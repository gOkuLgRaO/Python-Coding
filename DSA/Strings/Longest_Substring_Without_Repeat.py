def length_of_longest_substring(s):
    char_set = set()  # To store the characters in the current window
    left = 0 # left pointer for the windows
    max_length = 0 # To keep track of the maximum length of the substring. 

    # right pointer moves through the string 
    for right in range(len(s)):
        # If the character is already in the set, remove the characters from the left until the duplicate is removed.
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1

        # Add the current character to the set and update the max_length
        char_set.add(s[right])
        max_length = max(max_length, right - left + 1)

    return max_length


# Example Usage:
s = "abcabcbb"
print(length_of_longest_substring(s))  # Output: 3

s = "bbbbb"
print(length_of_longest_substring(s))  # Output: 1

s = "pwwkew"
print(length_of_longest_substring(s))  # Output: 3

"""
Approach: Sliding Window + Hash Set
The key idea is to use the sliding window technique to track the longest substring without repeating characters. We use two pointers (left and right) to represent the window, and a set to track the characters inside the window. As we expand the window by moving the right pointer, we adjust the window by moving the left pointer when we encounter a repeating character.

Explanation:
Initialize Variables:

char_set: A set to store the characters in the current window (substring).
left: The left pointer for the sliding window.
max_length: Stores the length of the longest substring found so far.
Sliding Window Expansion:

The right pointer iterates through the string character by character.
If s[right] is not in the char_set, it means there are no duplicates in the current window, so we can safely add s[right] to char_set.
If s[right] is in char_set, we move the left pointer to the right, removing characters from the set until s[right] is no longer in the set.
Update Maximum Length:

After adding a character to char_set, update max_length to store the maximum length of the substring encountered so far.
Return the Result:

The final value of max_length is the length of the longest substring without repeating characters.
Example Walkthrough:
Consider the input s = "abcabcbb":

Initialize left = 0, right = 0, max_length = 0, and char_set = {}.
Expand the window as the right pointer moves:
When right = 0, the window contains "a", char_set = {'a'}, max_length = 1.
When right = 1, the window contains "ab", char_set = {'a', 'b'}, max_length = 2.
When right = 2, the window contains "abc", char_set = {'a', 'b', 'c'}, max_length = 3.
When right = 3, s[right] is "a" which is already in the char_set. Remove characters starting from left until "a" is removed from the set, i.e., move left to 1.
Continue expanding and adjusting the window as needed.
The maximum length of the substring without repeating characters is 3.
"""
