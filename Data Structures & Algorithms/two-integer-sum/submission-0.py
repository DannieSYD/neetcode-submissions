class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i, num in enumerate(nums):
            res = target - num
            if res not in dic:
                dic[num] = i
            else:
                return [dic[res], i]