/**
 *  https://leetcode.com/problems/running-sum-of-1d-array/
 * 
 * Given an array nums. We define a running sum of an array as running
 * Sum[i] = sum(nums[0]…nums[i]).
 * Return the running sum of nums.
 * 
 */


function runningSum(nums: number[]): number[] {
    const result: number[] = Array(nums.length).fill(0);
    let sum = 0;
    for (let i = 0; i < nums.length; i++) {
        sum += nums[i];
        result[i] = sum;
    }
    return result;
};

function tests() {
    let nums = [1,2,3,4];
    let expected = [1,3,6,10];
    let result = runningSum(nums);
    console.assert(JSON.stringify(result) === JSON.stringify(expected), `Test case 1 failed: runningSum(${JSON.stringify(nums)}) = ${JSON.stringify(result)}, expected ${JSON.stringify(expected)}`);
    console.log(`Test case 1 passed: runningSum(${JSON.stringify(nums)}) = ${JSON.stringify(result)}`);

    nums = [1,1,1,1,1];
    expected = [1,2,3,4,5];
    result = runningSum(nums);
    console.assert(JSON.stringify(result) === JSON.stringify(expected), `Test case 2 failed: runningSum(${JSON.stringify(nums)}) = ${JSON.stringify(result)}, expected ${JSON.stringify(expected)}`);
    console.log(`Test case 2 passed: runningSum(${JSON.stringify(nums)}) = ${JSON.stringify(result)}`);

    nums = [3,1,2,10,1];
    expected = [3,4,6,16,17];
    result = runningSum(nums);
    console.assert(JSON.stringify(result) === JSON.stringify(expected), `Test case 3 failed: runningSum(${JSON.stringify(nums)}) = ${JSON.stringify(result)}, expected ${JSON.stringify(expected)}`);
    console.log(`Test case 3 passed: runningSum(${JSON.stringify(nums)}) = ${JSON.stringify(result)}`);
}

tests();