
from typing import List

# https://leetcode.com/problems/two-sum/description/

"""
Given an array of integers nums and an integer target, 
return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, 
and you may not use the same element twice.
You can return the answer in any order.
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h = {}
        for ind, num in enumerate(nums):
            r = target - num
            if r in h and h[r] != ind:
                return [h[r], ind]
            h[num] = ind

        return []


if __name__ == '__main__':
    s = Solution()
    assert s.twoSum([2, 7, 11, 15], 9) == [0, 1]
    assert s.twoSum([3, 2, 4], 6) == [1, 2]
    assert s.twoSum([3, 3], 6) == [0, 1]
    assert s.twoSum([3, 2, 3], 6) == [0, 2]
    assert s.twoSum([1, 2, 3, 4, 5], 10) == []
