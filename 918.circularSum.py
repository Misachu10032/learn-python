from collections import deque

class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        counter =0
        curr=0
        length=len(nums)
        result=float('-inf')
        currentMax=0
        while counter<length:
            currentMax +=nums[curr]
            if currentMax>result:
                result=currentMax
            if currentMax<0:
                currentMax=0
                length -=1
                counter =-1
            curr +=1
            counter +=1
            if curr== length:
                curr=0
        return result


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
