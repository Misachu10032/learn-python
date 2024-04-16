from collections import deque

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        my_map = {"{": "}", "(": ")", "[": "]"}
        stack = deque()

        for char in s:
            if char in my_map:
                stack.append(my_map[char])
            else:
                if not stack or stack.pop() != char:
                    return False

        return not stack

# Instantiate the Solution class
solution = Solution()

# Test cases
test_cases = [
    "()",        # Valid case
    "()[]{}",    # Valid case
    "(]",        # Invalid case
    "([)]",      # Invalid case
    "{[]}",      # Valid case
]

# Run test cases
for test_case in test_cases:
    result = solution.isValid(test_case)
    print(f"Input: {test_case}, Result: {result}")
