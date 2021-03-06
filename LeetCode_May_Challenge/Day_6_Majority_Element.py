'''
Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.

Example 1:

Input: [3,2,3]
Output: 3
Example 2:

Input: [2,2,1,1,1,2,2]
Output: 2
'''
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
