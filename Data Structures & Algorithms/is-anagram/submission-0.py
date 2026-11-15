class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dic = {}
        t_dic = {}
        if len(s) == len(t) and len(s) != 0:
            for s_c in s:
                if s_c not in s_dic:
                    s_dic[s_c] = 1
                else:
                    s_dic[s_c] += 1
            for t_c in t:
                if t_c not in t_dic:
                    t_dic[t_c] = 1
                else:
                    t_dic[t_c] += 1
            if s_dic == t_dic:
                return True
            else:
                return False
        else:
            return False