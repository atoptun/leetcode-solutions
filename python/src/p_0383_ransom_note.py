# https://leetcode.com/problems/ransom-note/description/

from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazine_count = Counter(magazine)
        for char in ransomNote:
            if magazine_count[char] == 0:
                return False
            magazine_count[char] -= 1
        return True


if __name__ == '__main__':
    s = Solution()
    ransomNote = "a"
    magazine = "b"
    result = s.canConstruct(ransomNote, magazine)
    print(f'ransomNote={ransomNote}, magazine={magazine}, canConstruct={result}')
    assert result is False
    print('-' * 10)

    ransomNote = "aa"
    magazine = "ab"
    result = s.canConstruct(ransomNote, magazine)
    print(f'ransomNote={ransomNote}, magazine={magazine}, canConstruct={result}')
    assert result is False
    print('-' * 10)

    ransomNote = "aa"
    magazine = "aab"
    result = s.canConstruct(ransomNote, magazine)
    print(f'ransomNote={ransomNote}, magazine={magazine}, canConstruct={result}')
    assert result is True
    print('-' * 10)

