def canConstruct(ransomNote, magazine):
    for chars in ransomNote:
        if chars in magazine:
            magazine = magazine.replace(chars, '', 1)
            ransomNote = ransomNote.replace(chars, '', 1)
    return True if len(ransomNote) == 0 else False

ransomNote = "fffbfg"
magazine = "effjfggbffjdgbjjhhdegh"

print(canConstruct(ransomNote, magazine)