'''
Given a positive integer num, write a function which returns True if num is a perfect square else False.

Follow up: Do not use any built-in library function such as sqrt.

Example 1:

Input: num = 16
Output: true
Example 2:

Input: num = 14
Output: false
 
Constraints:

1 <= num <= 2^31 - 1
'''
from typing import List
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
        