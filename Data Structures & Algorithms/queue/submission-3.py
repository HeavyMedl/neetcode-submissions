class Node:
    def __init__(self, value: int, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

class Deque:
    def __init__(self):
        self.head = Node(-1)
        self.tail = Node(-1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def isEmpty(self) -> bool:
        if self.head.next == self.tail:
            return True
        return False
        
    def append(self, value: int) -> None:
        node = Node(value, self.tail.prev, self.tail)
        self.tail.prev.next = node
        self.tail.prev = node

    def appendleft(self, value: int) -> None:
        node = Node(value, self.head, self.head.next)
        self.head.next.prev = node
        self.head.next = node

    def pop(self) -> int:
        if self.isEmpty():
            return -1
        
        node = self.tail.prev
        node.prev.next = node.next
        node.next.prev = node.prev

        return node.value

    def popleft(self) -> int:
        if self.isEmpty():
            return -1
        
        node = self.head.next
        node.next.prev = node.prev
        node.prev.next = node.next

        return node.value
        
