
class Solution:
    def frequencySort(self, s: str) -> str:
        mydict = dict()
        for i, c in enumerate(s):
            if c in mydict.keys():
                mydict[c]+=1
            else:
                mydict[c] = 1

        sorted_dict = {k: v for k, v in sorted(mydict.items(), key=lambda item: item[1], reverse=True)}
        # sortedDict = sorted(mydict.keys())
        list_c = []
        for c in sorted_dict.keys():
            list_c.append(c*sorted_dict[c])
        return ''.join(list_c)
        
        

str1 = "tree"
str2 = "Aabb"
print(Solution().frequencySort(str1))
print(Solution().frequencySort(str2))