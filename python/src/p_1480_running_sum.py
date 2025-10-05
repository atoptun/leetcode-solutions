from typing import List

#   https://leetcode.com/problems/running-sum-of-1d-array/
 
#  Given an array nums. We define a running sum of an array as running
#  Sum[i] = sum(nums[0]…nums[i]).
#  Return the running sum of nums.


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        result = [0] * len(nums)
        s = 0
        for i, n in enumerate(nums):
            s += n
            result[i] = s
        return result

if __name__ == '__main__':
    s = Solution()
    assert s.runningSum([1, 2, 3, 4]) == [1, 3, 6, 10]
    assert s.runningSum([1, 1, 1, 1, 1]) == [1, 2, 3, 4, 5]
    assert s.runningSum([3, 1, 2, 10, 1]) == [3, 4, 6, 16, 17]
    assert s.runningSum([1]) == [1]
    assert s.runningSum([]) == []
    assert s.runningSum([1, -1, 1, -1]) == [1, 0, 1, 0]
