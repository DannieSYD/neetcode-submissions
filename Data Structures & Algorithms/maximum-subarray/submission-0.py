class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        f, m = 0, float('-inf')
        for n in nums:
            f = max(n, f+n)
            m = max(m, f)
        return m
      
        