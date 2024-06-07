class Solution(object):
    def maxProduct(self, nums):
        
        ptr = 1
        maxVal = 0

        for num in nums:

            if(ptr < 0): 
                ptr = 0
            else:
                ptr *= num
            
            maxVal = max(maxVal, ptr)
        
        return maxVal
