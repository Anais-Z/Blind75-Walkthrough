
# Question Description

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 
Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]


# **How to Solve it:**


Initialize a hashmap: This will store each number and its index as we iterate through the array.

## **Iterate through the array:**

For each current number (num), calculate its complement (n) such that n = target - num.

## **Check if n is already a key in the hashmap:**

If n is found, it means we have already seen a number which, when added to the current number (num), equals the target. Retrieve the index of n from the hashmap.

If n is not found, add the current number (num) as a key and its index as the value to the hashmap.

## **Return the indices:**

If a match is found (i.e., n is in the hashmap), return the index of n (from the hashmap) and the current index.

This approach ensures an O(n) runtime because each lookup and insertion operation in the hashmap is O(1).

**Video Reference::** https://www.youtube.com/watch?v=KLlXCFG5TnA
