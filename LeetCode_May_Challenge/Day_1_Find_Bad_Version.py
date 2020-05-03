def isBadVersion(n):
    if n >=1:
        return True
    return False

def firstBadVersion(n):
    """
    :type n: int
    :rtype: int
    """
    left = 0
    right = n
    while left < right:
        mid = left + (right - left)// 2
        if isBadVersion(mid):
            right = mid
        else:
            left = mid+1
    
    if left == right and isBadVersion(left):
        return left
    
    return -1

n = 2
print(firstBadVersion(n))