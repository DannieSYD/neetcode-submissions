class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        for s in strs:
            s_sorted = str(sorted(s))
            if s_sorted in dic:
                dic[s_sorted].append(s)
            else:
                dic[s_sorted] = [s]

        return list(dic.values())
        