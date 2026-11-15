class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        f_dic = {}
        for num in nums:
            if num not in f_dic:
                f_dic[num] = 1
            else:
                f_dic[num] += 1
        freq = sorted(list(f_dic.keys()), key=lambda x: f_dic[x], reverse=True)
        return freq[:k]
        

        
        