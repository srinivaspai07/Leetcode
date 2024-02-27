class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        if not prices:
            return 0

        min_price = prices[0]
        max_profit = 0

        for price in prices:
            # Update min_price if the current price is lower
            min_price = min(min_price, price)
            # Update max_profit if selling at the current price yields a higher profit
            max_profit = max(max_profit, price - min_price)

        return max_profit
