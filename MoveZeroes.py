def moveZeroes(nums):
    count = 0
    for i in range(len(nums)): 
        if nums[i] != 0:
            nums[count] = nums[i]
            count+=1
    while count < len(nums): 
        nums[count] = 0
        count += 1

print(moveZeroes([1,2, 3, 4, 0, 0]))