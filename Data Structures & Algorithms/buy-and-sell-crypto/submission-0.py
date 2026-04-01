class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price, max_profit = prices[0], 0
        
        for price in prices:
            max_profit = max(max_profit, price-min_price)
            min_price = min(min_price, price)
        
        return max_profit