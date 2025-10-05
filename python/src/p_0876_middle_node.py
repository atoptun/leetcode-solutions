from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

if __name__ == '__main__':
    s = Solution()

    # Example 1
    n = [1, 2, 3, 4, 5]
    head = ListNode(n[0], ListNode(n[1], ListNode(n[2], ListNode(n[3], ListNode(n[4])))))
    print(f'list={n}')
    mid = s.middleNode(head)
    print(f'middle node={mid.val}')
    assert mid.val == 3
    print('-' * 10)

    # Example 2
    n = [1, 2, 3, 4, 5, 6]
    head = ListNode(n[0], ListNode(n[1], ListNode(n[2], ListNode(n[3], ListNode(n[4], ListNode(n[5]))))))
    print(f'list={n}')
    mid = s.middleNode(head)
    print(f'middle node={mid.val}')
    assert mid.val == 4
    print('-' * 10)

    # Example 3
    n = [1]
    head = ListNode(n[0])
    print(f'list={n}')
    mid = s.middleNode(head)
    print(f'middle node={mid.val}')
    assert mid.val == 1
    print('-' * 10)

    # Example 4
    n = [1, 2]
    head = ListNode(n[0], ListNode(n[1]))
    print(f'list={n}')
    mid = s.middleNode(head)
    print(f'middle node={mid.val}')
    assert mid.val == 2
    print('-' * 10)
