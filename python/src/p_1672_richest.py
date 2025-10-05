from typing import List

# 1672. Richest Customer Wealth
# https://leetcode.com/problems/richest-customer-wealth/description/

"""
You are given an m x n integer grid accounts where accounts[i][j] 
is the amount of money the i​​​​​​​​​​​th​​​​ customer has in the j​​​​​​​​​​​th​​​​ bank. 
Return the wealth that the richest customer has.

A customer's wealth is the amount of money they have in all their bank accounts. 
The richest customer is the customer that has the maximum wealth.
"""

class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_wealth = 0
        for account in accounts:
            wealth = sum(account)
            if wealth > max_wealth:
                max_wealth = wealth
        return max_wealth



if __name__ == '__main__':
    s = Solution()
    assert s.maximumWealth([[1, 2, 3], [3, 2, 1]]) == 6
    assert s.maximumWealth([[1, 5], [7, 3], [3, 5]]) == 10
    assert s.maximumWealth([[2, 8, 7], [7, 1, 3], [1, 9, 5]]) == 17
    assert s.maximumWealth([[1, 2], [3, 4], [5, 6]]) == 11
    assert s.maximumWealth([[1]]) == 1
    print('All tests passed.')
