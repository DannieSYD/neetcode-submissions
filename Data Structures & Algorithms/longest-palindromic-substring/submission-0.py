class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = s[0]
            # ccabac
            # for i, c in enumerate(s): O(n)
            #   l, r = i, i
            #   while l >= 0 and r < len(s) and s[l] == s[r]: O(n)
            #.     res = max(len(res), l-r) 
            #.     l -= 1
            #.     r += 1
            # ababd
            # res a
            # i, c 1, b
            # l, r 1, 1
            # l, r 0, 2
            # res aba
        for i, c in enumerate(s):
            # odd number
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r-l+1) > len(res):
                    res = s[l : r + 1]
                l -= 1
                r += 1
            
            # even number
            if i < len(s)-1 and c == s[i + 1]:
                l, r = i, i+1
                while l >= 0 and r < len(s) and s[l] == s[r]:
                    if (r-l+1) > len(res):
                        res = s[l : r + 1]
                    l -= 1
                    r += 1

        return res


        