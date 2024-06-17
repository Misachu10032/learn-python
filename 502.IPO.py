from typing import List


class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        n = len(profits)
        projects = [( profits[i],capital[i]) for i in range(n)]
        projects.sort(key=lambda x: (-x[0], x[1]))
        print(projects)
        result=w
        while k>0:
            i=0
            while i<n and n>0:
                if projects[i][1]<= result:
                    result += projects[i][0]
                    projects.pop(i)
                    n -=1
                    break
                i +=1
            # if i == n:
            #     return result
            k -=1
        return result
solution = Solution()

profits =[1,2,3]
capital =[0,1,1]


result = solution.findMaximizedCapital(2,0,profits,capital)
print(result)


# class Solution:
#     def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
#         n = len(profits)
#         projects = [(capital[i], profits[i]) for i in range(n)]
#         projects.sort()
#         i = 0
#         maximizeCapital = []
#         while k > 0:
#             while i < n and projects[i][0] <= w:
#                 heapq.heappush(maximizeCapital, -projects[i][1])
#                 i += 1
#             if not maximizeCapital:
#                 break
#             w -= heapq.heappop(maximizeCapital)
#             k -= 1
#         return w