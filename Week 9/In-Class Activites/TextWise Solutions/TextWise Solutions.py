"""
Enhancing internal tool through recursion, The core task is to reverse a string where the function calling itself with a subset of the original problem until a base case is reached.


Qs
Input Constraints: Are there any limitations on the string's length? Knowing this helps understand the recursion depth.
Character Set: Does the string include only ASCII characters, or should it support Unicode (including emojis, etc.)?
Performance Expectations: What is the expected performance in terms of time and space complexity? This could influence optimization strategies.

Time Complexity: O(n), Space Complexity: O(n)
"""


def reverse_string(s):
    # Base case: an empty string or a single character string is returned as is
    if len(s) <= 1:
        return s

    # Recursive step: reverse the substring excluding the first character,
    # and then append the first character to the end
    return reverse_string(s[1:]) + s[0]
print(reverse_string("hello dolly"))  # Should print: ylloD olleH

