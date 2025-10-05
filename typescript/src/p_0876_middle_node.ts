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


function middleNode(head: ListNode | null): ListNode | null {
    if (!head) return null;

    let slow: ListNode | null = head;
    let fast: ListNode | null = head;

    while (fast && fast.next) {
        slow = slow!.next;
        fast = fast.next.next;
    }

    return slow;
};

function tests() {
    let head = new ListNode(1, new ListNode(2, new ListNode(3, new ListNode(4, new ListNode(5)))));
    let expected = 3;
    let result = middleNode(head);
    console.assert(result?.val === expected, `Test case 1 failed: middleNode(${head}) = ${result?.val}, expected ${expected}`);
    console.log(`Test case 1 passed: middleNode(${head}) = ${result?.val}`);

    head = new ListNode(1, new ListNode(2, new ListNode(3, new ListNode(4, new ListNode(5, new ListNode(6))))));
    expected = 4;
    result = middleNode(head);
    console.assert(result?.val === expected, `Test case 2 failed: middleNode(${head}) = ${result?.val}, expected ${expected}`);
    console.log(`Test case 2 passed: middleNode(${head}) = ${result?.val}`);

    head = new ListNode(1);
    expected = 1;
    result = middleNode(head);
    console.assert(result?.val === expected, `Test case 3 failed: middleNode(${head}) = ${result?.val}, expected ${expected}`);
    console.log(`Test case 3 passed: middleNode(${head}) = ${result?.val}`);
}

tests();