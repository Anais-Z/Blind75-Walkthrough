class Solution(object):
    def maxSubArray(self, nums):
       
       ptr1 = 0
       maxNum = nums[0]

       for num in nums:
            # Expand or reset the window
            if ptr1 < 0:
                ptr1 = num  # Start a new subarray
            else:
                ptr1 += num  # Extend the current subarray
            
            # Update the maximum subarray sum
            maxNum = max(maxNum, ptr1)

       return maxNum
