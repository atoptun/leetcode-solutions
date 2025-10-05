# https://leetcode.com/problems/remove-element/

from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k



def tests():
    s = Solution()

    nums = [3, 2, 2, 3]
    val = 3
    k = s.removeElement(nums, val)
    print(f'nums={nums}, val={val}, k={k}')
    assert k == 2
    assert nums[:k] == [2, 2]
    print('-' * 10)

    nums = [0,1,2,2,3,0,4,2]
    val = 2
    k = s.removeElement(nums, val)
    print(f'nums={nums}, val={val}, k={k}')
    assert k == 5
    assert nums[:k] == [0,1,3,0,4]
    print('-' * 10)

    nums = []
    val = 0
    k = s.removeElement(nums, val)
    print(f'nums={nums}, val={val}, k={k}')
    assert k == 0
    assert nums[:k] == []
    print('-' * 10)

    nums = [1]
    val = 1
    k = s.removeElement(nums, val)
    print(f'nums={nums}, val={val}, k={k}')
    assert k == 0
    assert nums[:k] == []
    print('-' * 10)

    nums = [1]
    val = 0
    k = s.removeElement(nums, val)
    print(f'nums={nums}, val={val}, k={k}')
    assert k == 1
    assert nums[:k] == [1]
    print('-' * 10)


if __name__ == '__main__':
    tests()
