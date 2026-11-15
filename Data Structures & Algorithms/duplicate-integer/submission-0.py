class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # hash table
        hash_dic = {}
        for i, num in enumerate(nums):
            if num in hash_dic:
                return True
            else:
                hash_dic[num] = i
        return False
        