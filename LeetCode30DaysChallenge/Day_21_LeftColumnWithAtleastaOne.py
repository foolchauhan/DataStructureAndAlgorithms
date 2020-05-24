# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, x: int, y: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        n, m = binaryMatrix.dimensions()
        result = m
        
        def find(row):
            left=0
            right=m
            while left<right:
                mid = (left+right)//2
                
                if binaryMatrix.get(row, mid) == 0:
                    left = mid + 1
                else:
                    right = mid
            return left
        
        for i in range(n):
            col = find(i)
            result = min(result, col)
            
        if result == m:
            return -1
        
        return result
    