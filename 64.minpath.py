from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        for i in range(n):
            if i==0:
                for j in range(1,m):
                    grid[i][j]+=grid[i][j-1]
                continue

            for j in range(m):
                if j==0:
                    grid[i][j] +=grid[i-1][j]
                    continue
                grid[i][j] += min(grid[i-1][j],grid[i][j-1])
        print(grid)
        return grid[-1][-1]
    
solution = Solution()
nums =[[1,2,3],[4,5,6]]
result = solution.minPathSum(nums)