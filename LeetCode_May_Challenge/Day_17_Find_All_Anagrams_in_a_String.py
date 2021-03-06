'''
Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.

Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.

The order of output does not matter.

Example 1:

Input:
s: "cbaebabacd" p: "abc"

Output:
[0, 6]

Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
Example 2:

Input:
s: "abab" p: "ab"

Output:
[0, 1, 2]

Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".
'''
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
        