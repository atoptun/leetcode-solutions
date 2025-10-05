from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val: int = 0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result = ListNode(0)
        curr = result
        lr = 0
        while l1 is not None or l2 is not None or lr > 0:
            sum = l1.val if l1 else 0
            sum += l2.val if l2 else 0
            sum += lr
            curr.next = ListNode(sum % 10)
            curr = curr.next
            lr = sum // 10
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return result.next


def node_to_int(node: ListNode | None) -> int:
    n = node
    result = 0
    m = 1
    while n is not None:
        result += n.val * m
        m *= 10
        n = n.next
    return result


if __name__ == "__main__":
    s = Solution()
    l1 = ListNode(2, ListNode(4, ListNode(3)))
    assert node_to_int(l1) == 342
    l2 = ListNode(5, ListNode(6, ListNode(4)))
    assert node_to_int(l2) == 465
    r = s.addTwoNumbers(l1, l2)
    print(f'{node_to_int(l1)} + {node_to_int(l2)} = {node_to_int(r)}')
    assert node_to_int(l1) + node_to_int(l2) == node_to_int(r)

    s = Solution()
    l1 = ListNode(2, ListNode(4))
    l2 = ListNode(5, ListNode(6, ListNode(4)))
    r = s.addTwoNumbers(l1, l2)
    print(f'{node_to_int(l1)} + {node_to_int(l2)} = {node_to_int(r)}')
    assert node_to_int(l1) + node_to_int(l2) == node_to_int(r)

    s = Solution()
    l1 = ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9)))))))
    l2 = ListNode(9, ListNode(9, ListNode(9, ListNode(9))))
    r = s.addTwoNumbers(l1, l2)
    print(f'{node_to_int(l1)} + {node_to_int(l2)} = {node_to_int(r)}')
    assert node_to_int(l1) + node_to_int(l2) == node_to_int(r)
    