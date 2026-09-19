class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minIndex,maxIndex = 0,0
        maxProfit,currMax = 0,0
        for i in range(len(prices)):
            if prices[i] <= prices[minIndex]:
                minIndex,maxIndex = i,i
            if prices[i] >= prices[maxIndex]:
                maxIndex = i
                currMax = prices[maxIndex] - prices[minIndex]
                maxProfit = max(maxProfit,currMax)
        return maxProfit

        