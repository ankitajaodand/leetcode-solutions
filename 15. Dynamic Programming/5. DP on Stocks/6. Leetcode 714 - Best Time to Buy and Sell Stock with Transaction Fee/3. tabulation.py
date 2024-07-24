"""
Time Complexity: O(N*2) 
Reason: There are two nested loops that account for O(N*2) complexity.

Space Complexity: O(N*2)
Reason: We are using an external array of size 'N*2'. Stack Space is eliminated.
"""

from typing import List


class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        dp = [[-1, -1] for _ in range(n + 1)]
        dp[n][0] = dp[n][1] = 0
        for ind in range(n - 1, -1, -1):
            for buy in range(0, 2):
                profit = 0
                if buy:
                    buy_profit = -prices[ind] + dp[ind + 1][0]
                    not_buy_profit = 0 + dp[ind + 1][1]
                    profit = max(buy_profit, not_buy_profit)
                else:
                    sell_profit = prices[ind] + dp[ind + 1][1] - fee
                    not_sell_profit = 0 + dp[ind + 1][0]
                    profit = max(sell_profit, not_sell_profit)
                dp[ind][buy] = profit
        return dp[0][1]
