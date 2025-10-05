class Solution:
    def numberOfSteps(self, num: int) -> int:
        if num == 0:
            return 0
        return num.bit_length() - 1 + num.bit_count()


if __name__ == '__main__':
    s = Solution()
    n = 14
    print(f'n={n}, steps={s.numberOfSteps(n)}')
    assert s.numberOfSteps(n) == 6
    print('-' * 10)

    n = 8
    print(f'n={n}, steps={s.numberOfSteps(n)}')
    assert s.numberOfSteps(n) == 4
    print('-' * 10)

    n = 123
    print(f'n={n}, steps={s.numberOfSteps(n)}')
    assert s.numberOfSteps(n) == 12
    print('-' * 10)

    n = 0
    print(f'n={n}, steps={s.numberOfSteps(n)}')
    assert s.numberOfSteps(n) == 0
    print('-' * 10)

    n = 1
    print(f'n={n}, steps={s.numberOfSteps(n)}')
    assert s.numberOfSteps(n) == 1
    print('-' * 10)
