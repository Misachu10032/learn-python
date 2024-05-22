
from collections import deque

from typing import List

class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        queue=deque([startGene])
        seen=set()
        counter=0
        while queue:
            for _ in range(len(queue)):
                cur=queue.popleft()
                print(cur,"cur")
                print("\n")
                if cur == endGene:
                    return counter
                for word in bank:
                    if word in seen:
                        continue
                    mutationCount=0
                    for i in range(len(word)):
                        if cur[i] != word[i]:
                            mutationCount +=1
                        if mutationCount > 1:
                            continue
                    if mutationCount  == 1:
                        queue.append(word)
                        seen.add(word)
            counter +=1
            print(counter)

            print("\n")
            print(seen)
            print("\n")
    
        return -1
        

# Instantiate the Solution class
solution = Solution()

# Test cases
bank =["hot","dot","dog","lot","log","cog"]
end="dog"
start="hit"

result = solution.minMutation(start,end,bank)
print(result)

