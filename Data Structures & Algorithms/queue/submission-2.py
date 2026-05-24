class Node:
    def __init__(self, val: int, next=None):
        self.val = val
        self.next = next

class Deque:
    def __init__(self):
        dummy = Node(-1)
        self.head = self.tail = dummy

    def isEmpty(self) -> bool:
        return True if not self.head.next else False

    def append(self, value: int) -> None:
        self.tail.next = Node(value)
        self.tail = self.tail.next

    def appendleft(self, value: int) -> None:
        node = Node(value)
        node.next = self.head.next
        self.head.next = node

        if not node.next:
            self.tail = node

    def pop(self) -> int:
        if self.isEmpty():
            return -1
        #  h
        # (-1) -> (0) -> null
        #.         t
        curr = self.head
        while curr.next and curr.next != self.tail:
            curr = curr.next
        # curr should be the previous to tail node
        node = self.tail
        curr.next = curr.next.next
        self.tail = curr
        if not self.head.next:
            self.tail = self.head

        return node.val
        

    def popleft(self) -> int:
        if self.isEmpty():
            return -1
        
        #  h
        # (-1) -> (0) -> null
        #.         t
        node = self.head.next

        self.head.next = node.next

        if not self.head.next:
            self.tail = self.head

        return node.val
