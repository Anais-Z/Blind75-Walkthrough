Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

 

Example 1:

Input: nums = [1,2,3,1]
Output: true
Example 2:

Input: nums = [1,2,3,4]
Output: false
Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true

# How To Solve

**1.Sort the array in asending order** 

This will keep the values in the array in asending order, making the duplicates place beside each other in the array,

**2.Create 2 pointer vars**

Then in a while loop, match the values of the pointers in which they are indexed in the array.

If they don't match , increases the pointers vars by 1 (moving the pointers to the right of the array). If you reach the end but don't find a match return false.

But if you find a match, return true.



