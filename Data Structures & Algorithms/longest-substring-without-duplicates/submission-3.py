class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 1 or len(s) == 0:
            return len(s)
        else:
            i, j = 0, 1
            longest = 1
            current_l = 1
            while j < len(s):
                dup = s[i:j].find(s[j])
                if dup == -1:
                    j = j+1
                    current_l += 1
                    if current_l > longest:
                        longest = current_l
                else:
                    j = j+1
                    i = dup+1+i
                    current_l =  j - i
            return longest

