from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x: int, next: Optional['ListNode'] = None):
        self.val = x
        self.next = next


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        
        slow = head
        fast = head.next
        
        while fast and fast.next:
            if slow == fast:
                return True
            slow = slow.next
            fast = fast.next.next
        
        return False


def tests():
    # Test case 1: No cycle
    node3 = ListNode(3)
    node2 = ListNode(2, node3)
    node1 = ListNode(1, node2)
    s = Solution()
    assert not s.hasCycle(node1)
    print("Test case 1 passed") 
    print('-' * 10)

    # Test case 2: Cycle exists
    node3.next = node1  # Create a cycle
    assert s.hasCycle(node1)
    print("Test case 2 passed")
    print('-' * 10) 

    # Test case 3: Single node without cycle
    single_node = ListNode(1)
    assert not s.hasCycle(single_node)
    print("Test case 3 passed")
    print('-' * 10)

    # Test case 4: Single node with cycle
    single_node.next = single_node  # Create a cycle
    assert s.hasCycle(single_node)
    print("Test case 4 passed")
    print('-' * 10) 

    # Test case 5: Empty list
    assert not s.hasCycle(None)
    print("Test case 5 passed")
    print('-' * 10)


if __name__ == '__main__':
    tests()

    