class Solution(object):
    def maxProfit(self, prices):
        

         
        leftPointer = 0
        rightPointer = 1
        runningMax = 0
        while(rightPointer < len(prices)):
        
            if( (prices[rightPointer] - prices[leftPointer] )  > 0):
            
             runningMax = max(runningMax, prices[rightPointer] - prices[leftPointer])        
            else:
                leftPointer = rightPointer;

            rightPointer += 1;
          
        return runningMax;

