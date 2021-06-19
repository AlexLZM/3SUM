# 3SUM
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
# Example
Input: nums = [-1,0,1,2,-1,-4]

Output: [[-1,-1,2],[-1,0,1]]

# strategy
1. Build counter of nums
2. decompose the problem into 2 scenarios:
 - dulplicates in solution
 - no duplicates in solution
3. in first scenario: loop over counter, if count > 1, check if -number * 2 in counter
4. in second scenerio: 
 - outer loop: over sorted keys of counter, set the search range for second number 
 - inner loop: over search range, check if (-num) + (-num2) in counter

# Time complexity:
O(n<sup>2</sup>)
