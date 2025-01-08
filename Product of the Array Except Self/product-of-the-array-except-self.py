class Solution(object):
    def productExceptSelf(self, nums):
        
        left = []
        right = []
 

        for i in range(0, len(nums)):

            if i == 0:
                left.append(1)
            else:
                left.append(left[i - 1] * nums[i - 1])

        right = [1] * len(nums)

        for i in range(len(nums) - 2, -1, -1):
            right[i] = nums[i + 1] * right[1 + i]

        newArr = []
        for i in range(0, len(nums)):
            newArr.append(left[i] * right[i])

     
        return newArr



        
