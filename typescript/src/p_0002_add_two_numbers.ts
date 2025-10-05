import * as assert from 'node:assert';

/**
 * Definition for singly-linked list.
 */
class ListNode {
    val: number
    next: ListNode | null
    constructor(val?: number, next?: ListNode | null) {
        this.val = (val===undefined ? 0 : val)
        this.next = (next===undefined ? null : next)
    }
}

function addTwoNumbers(l1: ListNode | null, l2: ListNode | null): ListNode | null {
    let dn = new ListNode(0);
    let curr = dn;
    let lr = 0
    while (l1 !== null || l2 !== null || lr !== 0) {
        let l1Val = l1 !== null ? l1.val : 0;
        let l2Val = l2 !== null ? l2.val : 0;
        let sum = lr + l1Val + l2Val;
        curr.next = new ListNode(sum % 10);
        curr = curr.next;
        lr = Math.floor(sum / 10);
        l1 = l1 !== null ? l1.next : null;
        l2 = l2 !== null ? l2.next : null;
    }
    return dn.next;
};

function nodeToInt(node: ListNode | null): number {
    let num = 0;
    let base = 1;
    while (node !== null) {
        num += node.val * base;
        base *= 10;
        node = node.next;
    }
    return num;
}

// Example usage:

let l1 = new ListNode(2, new ListNode(4, new ListNode(3)));
let l2 = new ListNode(5, new ListNode(6, new ListNode(4)));
assert.strictEqual(nodeToInt(addTwoNumbers(l1, l2)), nodeToInt(l1) + nodeToInt(l2));
console.log(`Test case 1 passed: ${nodeToInt(l1)} + ${nodeToInt(l2)} = ${nodeToInt(addTwoNumbers(l1, l2))}`);

l1 = new ListNode(0);
l2 = new ListNode(0);
assert.strictEqual(nodeToInt(addTwoNumbers(l1, l2)), nodeToInt(l1) + nodeToInt(l2));
console.log(`Test case 2 passed: ${nodeToInt(l1)} + ${nodeToInt(l2)} = ${nodeToInt(addTwoNumbers(l1, l2))}`);

l1 = new ListNode(9, new ListNode(9, new ListNode(9, new ListNode(9, new ListNode(9, new ListNode(9, new ListNode(9)))))));
l2 = new ListNode(9, new ListNode(9, new ListNode(9, new ListNode(9))));
assert.strictEqual(nodeToInt(addTwoNumbers(l1, l2)), nodeToInt(l1) + nodeToInt(l2));
console.log(`Test case 3 passed: ${nodeToInt(l1)} + ${nodeToInt(l2)} = ${nodeToInt(addTwoNumbers(l1, l2))}`);
