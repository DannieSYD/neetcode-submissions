class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 1 or len(s) == 0:
            return len(s)
        else:
            lastInd = {}
            start = 0
            maxLength = 1
            for end in range(len(s)):
                if s[end] in lastInd and lastInd[s[end]] >= start:
                    start = lastInd[s[end]]+1
                else:
                    maxLength = max(maxLength, end-start+1)
                lastInd[s[end]] = end
            return maxLength

