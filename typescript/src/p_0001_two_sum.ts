import assert from 'node:assert';

// https://leetcode.com/problems/two-sum/description/


// Given an array of integers nums and an integer target, 
// return indices of the two numbers such that they add up to target.
// You may assume that each input would have exactly one solution, 
// and you may not use the same element twice.
// You can return the answer in any order.

function twoSum(nums: number[], target: number): number[] {
    const h: Map<number, number> = new Map();
    for (let i = 0; i < nums.length; i++) {
        let r = target - nums[i];
        if (h.has(r) && h.get(r) !== i) {
            return [h.get(r)!, i];  
        }
        h.set(nums[i], i);
    }
    
    return []
};


function test() {
    let nums = [2,7,11,15], target = 9;
    assert.deepStrictEqual(twoSum(nums, target), [0, 1]);
    console.log(`Test case 1 passed: twoSum(${JSON.stringify(nums)}, ${target}) = ${JSON.stringify(twoSum(nums, target))}`);

    nums = [3,2,4], target = 6;
    assert.deepStrictEqual(twoSum(nums, target), [1, 2]);
    console.log(`Test case 2 passed: twoSum(${JSON.stringify(nums)}, ${target}) = ${JSON.stringify(twoSum(nums, target))}`);

    nums = [3,3], target = 6;
    assert.deepStrictEqual(twoSum(nums, target), [0, 1]);
    console.log(`Test case 3 passed: twoSum(${JSON.stringify(nums)}, ${target}) = ${JSON.stringify(twoSum(nums, target))}`);

    nums = [3,2,4], target = 9;
    assert.deepStrictEqual(twoSum(nums, target), []);
    console.log(`Test case 4 passed: twoSum(${JSON.stringify(nums)}, ${target}) = ${JSON.stringify(twoSum(nums, target))}`);

    nums = [], target = 1;
    assert.deepStrictEqual(twoSum(nums, target), []);
    console.log(`Test case 5 passed: twoSum(${JSON.stringify(nums)}, ${target}) = ${JSON.stringify(twoSum(nums, target))}`);
}

test();
