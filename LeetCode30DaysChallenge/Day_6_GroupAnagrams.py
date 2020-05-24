def groupAnagrams(strs):
    groupedAnagrams = list()
    map = {}
    for current in strs:
        _sorted = ''.join(sorted(current))
        if _sorted not in map:
            map[_sorted]= []
        
        map[_sorted].append(current)
    
    for keys in map:
        groupedAnagrams.append(map[keys])

    return groupedAnagrams


strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(groupAnagrams(strs))