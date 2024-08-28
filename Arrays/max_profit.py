from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # keep track of max profit
        max_profit = 0
        # keep track of the cheapest day
        cheapest_day = prices[0]
        # iterate thru prices
        for curr_day in prices:
            # calc the profit
            profit = curr_day - cheapest_day
            # if the profit for this is greater than the max
            if profit > max_profit:
                # set max to be todays profit
                max_profit = profit
            # if the current price is less than the cheapest day
            if curr_day < cheapest_day:
                # set cheapest to be todays price
                cheapest_day = curr_day
        # return the max profit
        return max_profit
