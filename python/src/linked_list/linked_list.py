from typing import Optional

class Node:
    def __init__(self, value: int = 0, next: Optional['Node'] = None):
        self.value = value
        self.next = next


class MyLinkedList:

    def __init__(self):
        self.size = 0
        self.head: Optional[Node] = None
        self.tail: Optional[Node] = None
        

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        
        current = self.head
        for _ in range(index):
            current = current.next
        return current.value


    def addAtHead(self, val: int) -> None:
        new_node = Node(val, self.head)
        self.head = new_node
        if self.size == 0:
            self.tail = new_node
        self.size += 1

    def addAtTail(self, val: int) -> None:
        new_node = Node(val)
        if self.size == 0:
            self.head = new_node
        else:
            self.tail.next = new_node
        self.tail = new_node
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.size:
            return None
        if index == 0:
            self.addAtHead(val)
            return
        if index == self.size:
            self.addAtTail(val)
            return
        
        current = self.head
        for _ in range(index - 1):
            current = current.next
        new_node = Node(val, current.next)
        current.next = new_node
        self.size += 1
        

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return None
        if index == 0:
            self.head = self.head.next
            if self.size == 1:
                self.tail = None
            self.size -= 1
            return
        
        current = self.head
        for _ in range(index - 1):
            current = current.next
        current.next = current.next.next
        if index == self.size - 1:
            self.tail = current
        self.size -= 1
        

def tests():
    llist = MyLinkedList()
    llist.addAtHead(1)
    llist.addAtTail(3)
    llist.addAtIndex(1, 2)   # linked list becomes 1->2->3
    assert llist.get(1) == 2  # returns 2
    llist.deleteAtIndex(1)    # now the linked list is 1->3
    assert llist.get(1) == 3   # returns 3

    print("All tests passed.")


if __name__ == '__main__':
    tests()

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)