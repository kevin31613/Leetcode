class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        maxprice ,minprice = 0, prices[0]
        for price in prices:
            minprice = min(minprice, price)
            maxprice = max(maxprice, price-minprice)
                
        return maxprice

h = Solution()
prices = [7,1,5,3,6,4]
print(h.maxProfit(prices))