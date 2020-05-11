from typing import List
class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        count = [0 for i in range(N+1)]
        for item in trust:
            count[item[0]]-=1
            count[item[1]]+=1
        for i in range(1, N+1):
            if count[i] == N-1:
                return i
        return -1

N = 4
trust = [[1,3],[1,4],[2,3],[2,4],[4,3]]

print(Solution().findJudge(N, trust))