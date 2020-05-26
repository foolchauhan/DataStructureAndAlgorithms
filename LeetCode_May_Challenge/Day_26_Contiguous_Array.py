# Day_26_Contiguous_Array.py
'''
Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1.

Example 1:
Input: [0,1]
Output: 2
Explanation: [0, 1] is the longest contiguous subarray with equal number of 0 and 1.
Example 2:
Input: [0,1,0]
Output: 2
Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.
Note: The length of the given binary array will not exceed 50,000.
'''
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        mydict = dict() 
        sum = 0
        maxLen = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                sum+=1
            elif nums[i] == 0:
                sum-=1
            else:
                pass
            if (sum == 0): 
                maxLen = i + 1
            elif (sum) in mydict: 
                maxLen = max(maxLen, i - mydict[sum])

            if sum not in mydict: 
                mydict[sum] = i 
    
        return maxLen
        