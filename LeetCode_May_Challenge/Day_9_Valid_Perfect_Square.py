class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num == 1:
            return True
            
        x = num//2
        y = set([x])
        while x * x != num:
            x = (x + (num // x)) // 2
            if x in y: 
                return False
            y.add(x)
        return True
        