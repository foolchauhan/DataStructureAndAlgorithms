def maxSubArray(nums):
    max_current = max_global = nums[0]
    for i in range(len(nums)):
        if i>0:
            max_current = max(nums[i], nums[i]+max_current)
        if max_current > max_global:
            max_global = max_current
    return max_global

print(maxSubArray([1]))