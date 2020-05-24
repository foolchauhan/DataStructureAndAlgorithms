'''
Given two strings s1 and s2, write a function to return true if s2 contains the permutation of s1. In other words, one of the first string's permutations is the substring of the second string.

Example 1:

Input: s1 = "ab" s2 = "eidbaooo"
Output: True
Explanation: s2 contains one permutation of s1 ("ba").
Example 2:

Input:s1= "ab" s2 = "eidboaoo"
Output: False

Constraints:

The input strings only contain lower case letters.
The length of both given strings is in range [1, 10,000].

Hint #1  
Obviously, brute force will result in TLE. Think of something else.

Hint #2  
How will you check whether one string is a permutation of another string?
Hint #3  
One way is to sort the string and then compare. But, Is there a better way?

Hint #4  
If one string is a permutation of another string then they must one common metric. What is that?

Hint #5  
Both strings must have same character frequencies, if one is permutation of another. Which data structure should be used to store frequencies?

Hint #6  
What about hash table? An array of size 26?
'''
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        mapp = [0] * 26
        for c in s1:
            mapp[ord(c) - 97] += 1
        i, j, count_chars = 0, 0, len(s1)
        while j < len(s2):
            if mapp[ord(s2[j]) - 97] > 0:   
                count_chars -= 1
            mapp[ord(s2[j]) - 97] -= 1
            j += 1
            if count_chars == 0:
                return True
            if j - i == len(s1):
                if mapp[ord(s2[i]) - 97] >= 0:
                    count_chars += 1
                mapp[ord(s2[i]) - 97] += 1
                i += 1
                
        return False

s1 = "ab"
s2 = "eidboaooo"

print(Solution().checkInclusion(s1, s2))