from collections import defaultdict
from bisect import bisect_left
def three_sum(nums):
    # Build counter for nums
    counter = defaultdict(int)
    for num in nums:
        counter[num] += 1
    res = []
    # scenario 1, duplicates in solution
    for num in counter:
        if counter[num] > 1:
            if num == 0:
                if counter[0] > 2:
                    res.append([0, 0, 0])
            elif (nums3 := (-2 * num)) in counter:
                res.append([num, num, nums3])
    # secnario 2, no duplicates in solution
    nums = sorted(counter)
    for i, num in enumerate(nums):
        target = -num
        # set search range
        low, high = target - nums[-1], target/2
        # find index for low, high by binary search
        l = bisect_left(nums, low, i+1)
        r = bisect_left(nums, high, l)
        # inner loop, search for pairs sum to target
        for num2 in nums[l: r]:
            if (num3 := (target - num2)) in counter:
                res.append([num, num2, num3])
                
    return res
        
    
