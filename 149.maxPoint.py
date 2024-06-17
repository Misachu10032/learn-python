
from cmath import inf
from typing import List


# def maxPoints( points: List[List[int]]) -> int:
#     seen = set()
#     mapDict = {}
#     def addToDic(curr:tuple,i:int,j:int):
#         if curr not in mapDict:
#             mapDict[curr] = {i,j}
#         else:
#             if i not in mapDict[curr]:
#                 mapDict[curr].add(i)
#             if j not in mapDict[curr]:
#                 mapDict[curr].add(j)
                

#     for indexi,i in enumerate(points):
#             seen.add((i[0], i[1]))
#             for indexj,j in enumerate(points):
#                 if (j[0], j[1]) in seen:
#                     continue

#                 if (i[0]-j[0]) == 0:
#                     curr = ('inf', 'none', i[0])
#                     addToDic(curr,indexi,indexj)
#                     continue

#                 slope = (i[1]-j[1])/(i[0]-j[0])
#                 if slope == 0:
#                     curr = (0, i[1], 'none')
#                     addToDic(curr,indexi,indexj)
#                     continue
#                 y = i[1]-i[0]*slope
#                 x = -y/slope
#                 curr = (slope, y, x)
#                 addToDic(curr,indexi,indexj)
#     print(mapDict)
#     return max(len(s) for s in mapDict.values())
def maxPoints( points: List[List[int]]) -> int:
        # check for edge case
        if len(points)<3:
            return len(points)
        
        maxlen = 0
        for i in range(len(points)):
            line = {}
            for j in range(i+1,len(points)):
                y = points[i][1] - points[j][1]
                x = points[i][0] - points[j][0]
                
                # for finding the y-intercept (b)
                # b = points[i][0] if x == 0  else points[i][1] - ((y/x) * points[i][0])
                
                # use the slop as the hash map key
                slop = y/x if x!=0 else inf
                
                if slop in line:
                    line[slop]+= 1
                else:
                    line[slop] = 2 
                maxlen = max(line[slop] , maxlen)
        print(line)
        return maxlen

points = [[1, 1], [3, 2], [5, 3], [4, 1], [2, 3], [1, 4]]

a=maxPoints(points)
print(a)