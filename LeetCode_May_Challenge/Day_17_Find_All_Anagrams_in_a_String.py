class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s)==0:return []
        pri=[2, 3, 5, 11, 19, 23, 37, 47, 59, 79, 97, 113, 137, 163, 191, 223, 257, 293, 331, 353, 383, 431, 487, 541, 587, 631]
        dct={}
        res=[]
        for c in "qwertyuiopasdfghjklzxcvbnm":
            dct[c]=pri[ord(c)-ord("a")]
        target=0
        for i in p:
            target+=dct[i]
        ln=len(p)
        
        sm=0
        l=0
        for i in range(len(s)):
            sm+=dct[s[i]]
            l+=1
            if l==ln:
                if sm==target:res.append(i-ln+1)
                sm-=dct[s[i-ln+1]]
                l-=1
            
            
        return res
        