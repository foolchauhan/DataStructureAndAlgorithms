'''
Given an arbitrary ransom note string and another string containing letters from all the magazines, write a function that will return true if the ransom note can be constructed from the magazines ; otherwise, it will return false.

Each letter in the magazine string can only be used once in your ransom note.

Example 1:

Input: ransomNote = "a", magazine = "b"
Output: false
Example 2:

Input: ransomNote = "aa", magazine = "ab"
Output: false
Example 3:

Input: ransomNote = "aa", magazine = "aab"
Output: true
 
Constraints:

You may assume that both strings contain only lowercase letters.
'''

def canConstruct(ransomNote, magazine):
    for chars in ransomNote:
        if chars in magazine:
            magazine = magazine.replace(chars, '', 1)
            ransomNote = ransomNote.replace(chars, '', 1)
    return True if len(ransomNote) == 0 else False

ransomNote = "fffbfg"
magazine = "effjfggbffjdgbjjhhdegh"

print(canConstruct(ransomNote, magazine))