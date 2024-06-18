from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp=[1]*len(nums)
        for i in range(1,len(dp)):
            for j in range(0,i):
                if nums[j]<nums[i]:
                    dp[i]=max(dp[i],dp[j]+1)
        print(dp)
        return dp[-1]
    

solution = Solution()
nums =[1,3,6,7,9,4,10,5,6]
result = solution.lengthOfLIS(nums)