from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if len(triangle)==1:
            return triangle[0]
        n=len(triangle)
        for i in range(1,n):
            print(triangle)
            subL=len(triangle[i])
            for j in range(subL):
                if j==0:
                    triangle[i][j] +=triangle[i-1][j]
                    continue
                if j==subL-1:
                    triangle[i][j] +=triangle[i-1][j-1]
                    continue                   
                triangle[i][j] += min(triangle[i-1][j-1],triangle[i-1][j])
        return min(triangle[n-1])
    
solution = Solution()
nums =[[2],[3,4],[6,5,7],[4,1,8,3]]
result = solution.minimumTotal(nums)