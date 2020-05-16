from typing import List
class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        k = self.kadane(A)
        cs = 0
        for i in range(len(A)):
            cs += A[i]
            A[i] = -A[i]
        cs = cs + self.kadane(A)
        if cs > k and cs != 0:
            return cs
        return k

    def kadane(self, nums):
        cursum, maxsum = nums[0], nums[0]
        for n in nums[1:]:
            cursum = max(n, cursum+n)
            maxsum = max(cursum, maxsum)
        return maxsum

A = [5, -3, 5]
print(Solution().maxSubarraySumCircular(A))