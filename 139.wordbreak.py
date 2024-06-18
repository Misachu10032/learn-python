from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        foundSet=set()
        n = len(s)
        i=0
        while i < n-1:
            print(i)
            print('\n')
            for j in range(1,n-i+2):
                if j == n-i+1:
                    return False
                # print(i+j)
                # print('\n')
                if s[i:(i+j)] in wordDict:
                    print(s[i:(i+j)])
                    print('\n')
                    foundSet.add(s[i:(i+j)])
                    i +=j
                    break


        for i in wordDict:
            if i not in foundSet:
                return False

        return True
class Solution:
    def wordBreak(self, s, wordDict):
        dp = [False] * (len(s) + 1)
        dp[0] = True

        for i in range(1, len(s) + 1):
            for j in range(i):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
                    break
        return dp[-1]

                
solution = Solution()
wordDict =["cats","dog","sand","and","cat"]
s ="catsandog"
print(solution.wordBreak(s,wordDict))