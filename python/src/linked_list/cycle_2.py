from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x: int, next: Optional['ListNode'] = None):
        self.val = x
        self.next = next


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        
        slow = head
        fast = head
        
        # Detect if a cycle exists
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        else:
            return None  # No cycle
        
        # Find the entry point of the cycle
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        
        return slow


def tests():
    # Test case 1: No cycle
    node3 = ListNode(3)
    node2 = ListNode(2, node3)
    node1 = ListNode(1, node2)
    s = Solution()
    assert s.detectCycle(node1) is None
    print("Test case 1 passed") 
    print('-' * 10)

    # Test case 2: Cycle exists
    node3.next = node1  # Create a cycle
    assert s.detectCycle(node1) == node1
    print("Test case 2 passed")
    print('-' * 10) 

    # Test case 3: Single node without cycle
    single_node = ListNode(1)
    assert s.detectCycle(single_node) is None
    print("Test case 3 passed")
    print('-' * 10)

    # Test case 4: Single node with cycle
    single_node.next = single_node  # Create a cycle
    assert s.detectCycle(single_node) == single_node
    print("Test case 4 passed")
    print('-' * 10) 

    # Test case 5: Empty list
    assert s.detectCycle(None) is None
    print("Test case 5 passed")
    print('-' * 10)


if __name__ == '__main__':
    tests()
