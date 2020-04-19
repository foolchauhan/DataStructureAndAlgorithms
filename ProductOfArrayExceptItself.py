def productExceptSelf(nums):
    i, temp = 1, 1
    n = len(nums)
    prod = [1 for i in range(n)]
    for i in range(n): 
        prod[i] = temp 
        temp *= nums[i] 
    
    temp = 1
    
    for i in range(n - 1, -1, -1): 
        prod[i] *= temp 
        temp *= nums[i]
    
    return prod