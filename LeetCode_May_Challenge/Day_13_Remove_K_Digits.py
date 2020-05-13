# from typing import List
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        rr = []
        remove_digits_count = k
        for n in num:
            while remove_digits_count and rr and rr[-1] > n:
                rr.pop()
                remove_digits_count-=1
            rr.append(n)
        res = ''.join(rr[0:len(num)-k]).lstrip('0')
        if len(res):
            return res
        return '0'