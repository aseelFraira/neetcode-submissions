class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        cheapestStock = prices[0]

        for price in prices:
            currProfit = price - cheapestStock
            maxProfit = max(currProfit,maxProfit)
            cheapestStock = min(cheapestStock,price)

        return maxProfit


            

            
        