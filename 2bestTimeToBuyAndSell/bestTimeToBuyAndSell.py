# Best time to buy and sell - Google interview question (Leet code 121)
# Say you have an array for which the iTH element is the price of a given stock on day i.
# If you were only permitted to complete at most one transaction (i.e, buy one and sell one share of the stock).design an algorithm
# to find the maximum profit. Note that you cannot sell a stock before you buy one.
# input : [7,1,5,3,6,4], output: 5, Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit=6-1=5.
# not 7-1 = 6 are selling price needs to be larger than buying price
# two pointer concept l,r, l=buy, r = sell 7 > 1 1 - 7 -6 if l is greater than r then move l to r and r to +1 index
# now check again l = 1, r=5, maxprofit=4 update max profit, r = 3 maxprofit = 2no update, r = 6 maxprofit=5 update, r=4maxprofit=5 no update
# found maxprofit space complexity: O(1), time Complexity : O(n)

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        l, r = 0, 1
        maxProfit = 0

        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxProfit = max(maxProfit, profit)
            else:
                l = r # left pointer could be at the minimum
            r += 1

        return maxProfit

print(Solution().maxProfit([7,1,5,3,6,4]))

