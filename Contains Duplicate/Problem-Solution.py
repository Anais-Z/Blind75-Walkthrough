class Solution(object):
    def containsDuplicate(self, nums):
        
        nums.sort()

        ptr1 = 0
        ptr2 = 1

        while(ptr2 < len(nums)):

            if(nums[ptr1] == nums[ptr2]):
                return True

            ptr1 += 1
            ptr2 += 1
        
        return False
