from typing import List
class Solution:
    def firstUniqChar(self, s: str) -> int:
        mydict = {}
        res = -1
        for i, ss in enumerate(s):
            if ss not in mydict:
                mydict[ss] = 1
                res = i
            else:
                mydict[ss]+=1
        
        for i, ss in enumerate(s):
            if mydict[ss] == 1:
                return i
        return -1

s = "loveleetcode"

print(Solution().firstUniqChar(s))
            

            