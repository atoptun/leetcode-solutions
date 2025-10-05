// https://leetcode.com/problems/ransom-note/description/

import assert from "node:assert";


function canConstruct(ransomNote: string, magazine: string): boolean {
    const magazineCount = new Map<string, number>();
    for (const char of magazine) {
        magazineCount.set(char, (magazineCount.get(char) || 0) + 1);
    }

    for (const char of ransomNote) {
        if (!magazineCount.has(char) || magazineCount.get(char)! <= 0) {
            return false;
        }
        magazineCount.set(char, magazineCount.get(char)! - 1);
    }

    return true;
};


function tests() {
    let ransomNote = "a", magazine = "b";
    let expected = false;
    let result = canConstruct(ransomNote, magazine);
    assert.strictEqual(result, expected, `Test case 1 failed: canConstruct(${ransomNote}, ${magazine}) = ${result}, expected ${expected}`);
    console.log(`Test case 1 passed: canConstruct(${ransomNote}, ${magazine}) = ${result}`);

    ransomNote = "aa", magazine = "ab";
    expected = false;
    result = canConstruct(ransomNote, magazine);
    assert.strictEqual(result, expected, `Test case 2 failed: canConstruct(${ransomNote}, ${magazine}) = ${result}, expected ${expected}`);
    console.log(`Test case 2 passed: canConstruct(${ransomNote}, ${magazine}) = ${result}`);

    ransomNote = "aa", magazine = "aab";
    expected = true;
    result = canConstruct(ransomNote, magazine);
    assert.strictEqual(result, expected, `Test case 3 failed: canConstruct(${ransomNote}, ${magazine}) = ${result}, expected ${expected}`);
    console.log(`Test case 3 passed: canConstruct(${ransomNote}, ${magazine}) = ${result}`);
}

tests();

