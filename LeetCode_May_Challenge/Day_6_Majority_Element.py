from typing import List
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        threshold = len(nums)//2
        mydict = {}
        for i, n in enumerate(nums):
            if not n in mydict.keys():
                mydict[n] = 1
            else:
                mydict[n]+=1
        
        return max(mydict, key=mydict.get) 

nums = [2,2,1,1,1,2,2]

print(Solution().majorityElement(nums))
