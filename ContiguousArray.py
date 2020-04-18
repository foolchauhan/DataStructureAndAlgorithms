def findMaxLength(nums):
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
