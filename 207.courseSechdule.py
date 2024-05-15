from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = [[] for _ in range(numCourses)]
     
        for c1, c2 in prerequisites:
            adjList[c1].append(c2)
        print(adjList)
        print('\n')

        comp=[]
        def hasCycle(course)->bool:
            prereq=adjList[course]
            print('\n')

            print(prereq)
            print(adjList)
            if course in comp or prereq==[]:
                comp.append(course)
                return False
            if course in prereq:
                print('we here?')
                return True
            if adjList[prereq[-1]] != []:
                adjList[course].extend(adjList[prereq[-1]])
                for i in prereq:
                    if hasCycle(i):
                        return True
                return False
        
        for course in range(numCourses):
            print('we sdsddddddddhere?')
            if hasCycle(course)==True:
                print('we sdhere?')
                return False
        
        return True

    

solution = Solution()
tokens =[[1,0],[1,2],[0,1]]
result = solution.canFinish(3,tokens)
print(result)
