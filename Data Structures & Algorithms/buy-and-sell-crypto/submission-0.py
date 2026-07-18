class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minprice=prices[0]
        maxprofit=0

        for price in prices:
            if price<minprice:
                minprice=price
            
            profit=price-minprice
            maxprofit=max(maxprofit,profit)
        return maxprofit