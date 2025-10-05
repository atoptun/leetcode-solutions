import assert from "assert";

// 1672. Richest Customer Wealth
// https://leetcode.com/problems/richest-customer-wealth/description/


// You are given an m x n integer grid accounts where accounts[i][j] 
// is the amount of money the i​​​​​​​​​​​th​​​​ customer has in the j​​​​​​​​​​​th​​​​ bank. 
// Return the wealth that the richest customer has.

// A customer's wealth is the amount of money they have in all their bank accounts. 
// The richest customer is the customer that has the maximum wealth.

function maximumWealth(accounts: number[][]): number {
    let maxWealth = 0;
    for (let i = 0; i < accounts.length; i++) {
        const wealth = accounts[i].reduce((a, b) => a + b, 0);
        if (wealth > maxWealth) {
            maxWealth = wealth;
        }
    }
    return maxWealth;
};


function tests() {
    let accounts = [[1,2,3],[3,2,1]];
    let expected = 6;
    let result = maximumWealth(accounts);
    assert.strictEqual(result, expected, `Test case 1 failed: maximumWealth(${JSON.stringify(accounts)}) = ${result}, expected ${expected}`);
    console.log(`Test case 1 passed: maximumWealth(${JSON.stringify(accounts)}) = ${result}`);

    accounts = [[1,5],[7,3],[3,5]];
    expected = 10;
    result = maximumWealth(accounts);
    assert.strictEqual(result, expected, `Test case 2 failed: maximumWealth(${JSON.stringify(accounts)}) = ${result}, expected ${expected}`);
    console.log(`Test case 2 passed: maximumWealth(${JSON.stringify(accounts)}) = ${result}`);

    accounts = [[2,8,7],[7,1,3],[1,9,5]];
    expected = 17;
    result = maximumWealth(accounts);
    assert.strictEqual(result, expected, `Test case 3 failed: maximumWealth(${JSON.stringify(accounts)}) = ${result}, expected ${expected}`);
    console.log(`Test case 3 passed: maximumWealth(${JSON.stringify(accounts)}) = ${result}`);
}

tests();


