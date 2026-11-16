class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest = prices[0]
        max_profit = 0
        for price in prices:
            if lowest > price:
                lowest = price
            elif price - lowest > max_profit:
                max_profit = price - lowest
        return max_profit
        