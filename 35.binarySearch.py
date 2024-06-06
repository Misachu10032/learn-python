from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        a= target
        return self.recursive(nums,0,a)

        
    def recursive(self,nums,prefix,a):
      
        length=len(nums)
        print(prefix,length)
        if length == 0:
            return prefix
        if length == 1:
            if nums[0]==a:
                return prefix+1
            elif nums[0] > a:
                return prefix
            else:
                return prefix+1
        mid=length//2
        if nums[mid]==a:
            return mid+prefix
        if nums[mid] > a:
            return self.recursive(nums[:mid],prefix,a)
        else:
            print('we here')
            return self.recursive(nums[mid+1:],prefix+mid+1,a)
        

solution = Solution()

# Test cases
nums =[2,7,8,9,10]
target=9

# Run test cases
print(solution.searchInsert(nums,target))