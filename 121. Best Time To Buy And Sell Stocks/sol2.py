class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        b = prices[0]
        profit = 0
        for i in range(1, len(prices)):
            if b > prices[i]:
                b = prices[i]
            elif prices[i] - b > profit:
                profit = prices[i] - b
        return profit 