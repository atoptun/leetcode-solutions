from typing import List

# https://leetcode.com/problems/fizz-buzz/description/

"""
Given an integer n, return a string array answer (1-indexed) where:

answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
answer[i] == "Fizz" if i is divisible by 3.
answer[i] == "Buzz" if i is divisible by 5.
answer[i] == i (as a string) if none of the above conditions are true.
"""

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        result = [""] * n
        for i in range(1, n + 1):
            if i % 3 == 0 and i % 5 == 0:
                result[i - 1] = "FizzBuzz"
            elif i % 3 == 0:
                result[i - 1] = "Fizz"
            elif i % 5 == 0:
                result[i - 1] = "Buzz"
            else:
                result[i - 1] = str(i)
        return result


if __name__ == '__main__':
    s = Solution()
    assert s.fizzBuzz(3) == ["1", "2", "Fizz"]
    assert s.fizzBuzz(5) == ["1", "2", "Fizz", "4", "Buzz"]
    assert s.fizzBuzz(15) == ["1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz", "11", "Fizz", "13", "14", "FizzBuzz"]
    print('All tests passed.')