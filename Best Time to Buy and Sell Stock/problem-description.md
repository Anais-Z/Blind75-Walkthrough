You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

 

Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
Example 2:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.

# How To Solve It

There are many ways to solve it but this is my favorite (using the sliding window technique)

Due to how we are buying first and then selling, we can only move to the right in the array

So we must create 2 pointers (ptr1 and ptr2, ptr1 at the 1st index and ptr2 is at the 2nd)

We should also declare a var of maxProfit to 0

# Step 1
So we check the value of what the pointers point to in the array.

If the value of the ptr1 is greater than ptr2 then we shift each pointer by 1 index.

If ptr2 is greater than we subtract both pointers (ptr 2 -ptr1) to get the current profit and put it in a var called current.

# Step 2
Then we check if the current profit is greater than the maxProfit. If true then maxProfit = currentProfit.

Since there are more values in the array, we shift ptr2 to the right by 1 then repeat step 1. 

Do this until ptr2 reaches to the end of the array and return maxProfit

**Reference** : https://www.youtube.com/watch?v=1pkOgXD63yU&t=421s
