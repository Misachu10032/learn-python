
from collections import deque
from itertools import chain
from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        length=len(word)
        maxRow=len(board)
        maxCol=len(board[0])
        ans=[]
        def dfs(current,r,c,index,tempBoard):

            if index==length:
                if current==word:
                    ans.append('true')
                    return
                else: return
            if r>=maxRow or r<0 or c>=maxCol or c<0:
                return
            print(board)
            if board[r][c] != word[index]:
                return
            temp=tempBoard[r][c]
            tempBoard[r][c]='#'
            dfs(current+temp,r+1,c,index+1,tempBoard)
            dfs(current+temp,r-1,c,index+1,tempBoard)
            dfs(current+temp,r,c+1,index+1,tempBoard)
            dfs(current+temp,r,c-1,index+1,tempBoard)
            tempBoard[r][c]=temp

        for a in range(maxRow):
            for b in range(maxCol):
                dfs('',a,b,0,board)
        return True if len(ans)!=0 else False
# Instantiate the Solution class
solution = Solution()

# Test cases
board = [["C","A","A"],["A","A","A"],["B","C","D"]]
# Run test cases

result = solution.exist(board,'AAB')
print(result)

