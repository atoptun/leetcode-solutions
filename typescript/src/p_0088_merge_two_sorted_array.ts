/**
 * https://leetcode.com/problems/merge-sorted-array/description/
 * 
 * You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, 
 * and two integers m and n, representing the number of elements in nums1 and nums2 respectively.
 *
 * Merge nums1 and nums2 into a single array sorted in non-decreasing order.
 *
 * The final sorted array should not be returned by the function, 
 * but instead be stored inside the array nums1. To accommodate this, 
 * nums1 has a length of m + n, where the first m elements denote the elements 
 * that should be merged, and the last n elements are set to 0 and should be ignored. 
 * nums2 has a length of n.
 */

/**
 Do not return anything, modify nums1 in-place instead.
 */

import assert from 'node:assert';


function merge(nums1: number[], m: number, nums2: number[], n: number): void {
    let i = m - 1;
    let j = n - 1;
    let k = m + n - 1;
    while (i >= 0 && j >= 0) {
        if (nums1[i] > nums2[j]) {
            nums1[k--] = nums1[i--];
        } else {
            nums1[k--] = nums2[j--];
        }
    }
    while (j >= 0) {
        nums1[k--] = nums2[j--];
    }

}

function tests() {
    let nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3;
    merge(nums1, m, nums2, n);
    assert.deepStrictEqual(nums1, [1,2,2,3,5,6]);
    console.log(`Test case 1 passed: merge(${JSON.stringify(nums1)}, ${m}, ${JSON.stringify(nums2)}, ${n}) = ${JSON.stringify(nums1)}`);

    nums1 = [1], m = 1, nums2 = [], n = 0;
    merge(nums1, m, nums2, n);
    assert.deepStrictEqual(nums1, [1]);
    console.log(`Test case 2 passed: merge(${JSON.stringify(nums1)}, ${m}, ${JSON.stringify(nums2)}, ${n}) = ${JSON.stringify(nums1)}`);
    
    nums1 = [0], m = 0, nums2 = [1], n = 1;
    merge(nums1, m, nums2, n);
    assert.deepStrictEqual(nums1, [1]);
    console.log(`Test case 3 passed: merge(${JSON.stringify(nums1)}, ${m}, ${JSON.stringify(nums2)}, ${n}) = ${JSON.stringify(nums1)}`);

    
}

tests();