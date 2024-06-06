

from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        if len(nums)==1:
            if nums[0]==target:
                return [0,0]
            else:
                return[-1,-1]
        left=0
        right=len(nums)-1
        result=-1
        while left<=right:
            mid = (left+right)//2
            if nums[mid]==target:
                result = mid
                break
            
            if nums[mid] < target:
                left=mid+1
            else:
                right=mid-1
        
        if result == -1:
            return [-1,-1]

        i= result
        j= result
        array=[result,result]
        while i>=0:
            if nums[i]==target:
               array[0]=i
               i -=1
            else:
                i=-1
        
        
        while j<len(nums):
            if nums[j]==target:
               array[1]=j
               j +=1
            else:
                j =len(nums)


        return array
    


                    
                
        
    


                    
                
        

# Instantiate the Solution class
solution = Solution()

nums = [5,7,7,8,8,10]
result = solution.searchRange(nums,8)

print(result)