// https://leetcode.com/problems/remove-element/

import assert from "node:assert";

function removeElement(nums: number[], val: number): number {
    let k = 0;
    for (let i = 0; i < nums.length; i++) {
        if (nums[i] !== val) {
            nums[k] = nums[i];
            k++;
        }
    }
    return k;
};


function tests() {
    let nums = [3, 2, 2, 3];
    let val = 3;
    let expected = 2;
    let result = removeElement(nums, val);
    assert.strictEqual(result, expected, `Test case 1 failed: removeElement([${nums}], ${val}) = ${result}, expected ${expected}`);
    console.log(`Test case 1 passed: removeElement([${nums}], ${val}) = ${result}`);

    nums = [0,1,2,2,3,0,4,2];
    val = 2;
    expected = 5;
    result = removeElement(nums, val);
    assert.strictEqual(result, expected, `Test case 2 failed: removeElement([${nums}], ${val}) = ${result}, expected ${expected}`);
    console.log(`Test case 2 passed: removeElement([${nums}], ${val}) = ${result}`);

    nums = [1];
    val = 1;
    expected = 0;
    result = removeElement(nums, val);
    assert.strictEqual(result, expected, `Test case 3 failed: removeElement([${nums}], ${val}) = ${result}, expected ${expected}`);
    console.log(`Test case 3 passed: removeElement([${nums}], ${val}) = ${result}`);
}

tests();

