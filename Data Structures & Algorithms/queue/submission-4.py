class Node:
    def __init__(self, value: int):
        self.value = value
        self.next = None
        self.prev = None


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
        node = Node(value)
        self.tail.prev.next = node
        node.prev = self.tail.prev
        node.next = self.tail
        self.tail.prev = node
        

    def appendleft(self, value: int) -> None:
        node = Node(value)
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node
        node.prev = self.head

    def pop(self) -> int:
        if self.isEmpty():
            return -1
        
        node = self.tail.prev
        node.prev.next = self.tail
        self.tail.prev = node.prev

        node.next = None
        node.prev = None

        return node.value
            

    def popleft(self) -> int:
        if self.isEmpty():
            return -1
        
        node = self.head.next
        node.next.prev = self.head
        self.head.next = node.next

        node.next = None
        node.prev = None

        return node.value
        
