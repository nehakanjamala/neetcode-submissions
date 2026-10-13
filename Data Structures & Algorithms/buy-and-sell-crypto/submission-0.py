class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min = prices[0] #buy
        profit = 0
        for i in range(len(prices)):
            cur_profit = prices[i] - min
            if prices[i] < min:
                min = prices[i]
            if cur_profit > profit:
                profit = cur_profit
        return profit