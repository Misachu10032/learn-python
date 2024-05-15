
from collections import deque
from itertools import chain
from typing import List

class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        board.reverse()
        for i in range(1,len(board),2):
            board[i].reverse()
        arr = [None]+list(chain(*board))
        print(arr)
        print('\n')
        print('\n')
        print('\n')
        
        n=len(arr)-1
        queue=deque([1])
        seen={1}
        counter=0

        while queue:
            lenQ = len(queue)
            for _ in range(lenQ):
                cur=queue.popleft()
                if cur == n:
                    return counter
                
                for i in range(cur+1,min(cur+7,n+1)):
                    print("wehere")
                    next = arr[i] if arr[i] !=-1 else i   
                    
                    if next in seen: 
                        continue
                    seen.add(next)
                    
                    queue.append(next)
                counter +=1

        return -1

# Instantiate the Solution class
solution = Solution()

# Test cases
test_cases = [[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,35,-1,-1,13,-1],[-1,-1,-1,-1,-1,-1],[-1,15,-1,-1,-1,-1]]
# Run test cases

result = solution.snakesAndLadders(test_cases)
print(result)

