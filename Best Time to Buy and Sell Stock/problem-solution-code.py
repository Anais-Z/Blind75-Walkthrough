class Solution(object):
    def maxProfit(self, prices):
        
        ptr1 = 0

        ptr2 = 1

        maxProfit = 0

        while(ptr2 < len(prices)):
            
            if(prices[ptr1] < prices[ptr2]):

               profit = prices[ptr2] - prices[ptr1]

               if(profit > maxProfit):
                 maxProfit = profit
                 

               ptr2 += 1
            else:
                ptr1 += 1
                ptr2 += 1

        return maxProfit
