class Solution(object):
  
    def twoSum(self, nums, target):
       numArray = nums

       targetNumber = target

       hashNum = {}

       for i in range(len(numArray)):

        num2 = targetNumber - numArray[i]

        if(num2 in hashNum):

            keyIndex = hashNum[num2]

            return [i, keyIndex]
        else:
            hashNum[numArray[i]] = i
           
  
