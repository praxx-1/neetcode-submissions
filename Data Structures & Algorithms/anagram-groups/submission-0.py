class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}

        for x in strs:
            key = tuple(sorted(x))

            if key not in dic:
                dic[key] =[x]
            else:
                dic[key].append(x)
        return (list(dic.values()))