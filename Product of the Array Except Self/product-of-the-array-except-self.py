class Solution(object):
    def productExceptSelf(self, nums):
         
        length = len(nums)
        newArray = [1] * length

        preFix = 1
        postFix = 1

        # Calculate the prefix products and store them in newArray
        for i in range(length):
            newArray[i] = preFix
            preFix *= nums[i]
        
        # Calculate the postfix products and multiply them into newArray
        for i in range(length - 1, -1, -1):
            newArray[i] *= postFix
            postFix *= nums[i]

        return newArray



        
