from typing import List


# https://leetcode.com/problems/merge-sorted-array/description/
# You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, 
# and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

# Merge nums1 and nums2 into a single array sorted in non-decreasing order.

# The final sorted array should not be returned by the function, 
# but instead be stored inside the array nums1. To accommodate this, 
# nums1 has a length of m + n, where the first m elements denote the elements 
# that should be merged, and the last n elements are set to 0 and should be ignored. 
# nums2 has a length of n.

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        l1, l2, k = m - 1, n - 1, m + n - 1
        while l1 >= 0 and l2 >= 0:
            if nums1[l1] > nums2[l2]:
                nums1[k] = nums1[l1]
                l1 -= 1
            else:
                nums1[k] = nums2[l2]
                l2 -= 1
            k -= 1
        if l2 >= 0:
            nums1[0:l2 + 1] = nums2[0:l2 + 1]



if __name__ == '__main__':
    s = Solution()
    n1, m = [1, 2, 3, 0, 0, 0], 3
    n2, n = [2, 5, 6], 3
    print(f'n1={n1}, m={m}, n2={n2}, n={n}')
    s.merge(n1, m, n2, n)
    print(f'n1={n1}, n2={n2}')
    assert n1 == [1, 2, 2, 3, 5, 6]
    print('-' * 10)

    n1, m = [1], 1
    n2, n = [], 0
    print(f'n1={n1}, m={m}, n2={n2}, n={n}')
    s.merge(n1, m, n2, n)
    print(f'n1={n1}, n2={n2}')
    assert n1 == [1]
    print('-' * 10)

    n1, m = [0], 0
    n2, n = [1], 1
    print(f'n1={n1}, m={m}, n2={n2}, n={n}')
    s.merge(n1, m, n2, n)
    print(f'n1={n1}, n2={n2}')
    assert n1 == [1]
    print('-' * 10)

    n1, m = [4, 5, 6, 0, 0, 0], 3
    n2, n = [1, 2, 3], 3
    print(f'n1={n1}, m={m}, n2={n2}, n={n}')
    s.merge(n1, m, n2, n)
    print(f'n1={n1}, n2={n2}')
    assert n1 == [1, 2, 3, 4, 5, 6]
    print('-' * 10)

    n1, m = [2, 0], 1
    n2, n = [1], 1
    print(f'n1={n1}, m={m}, n2={n2}, n={n}')
    s.merge(n1, m, n2, n)
    print(f'n1={n1}, n2={n2}')
    assert n1 == [1, 2]
    print('-' * 10)
