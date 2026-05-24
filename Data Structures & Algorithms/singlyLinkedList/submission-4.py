class Node:
    def __init__(self, val, next_node=None):
        self.val = val
        self.next = next_node


class LinkedList:
    
    def __init__(self):
        self.head = Node(-1)
        self.tail = self.head
    
    def get(self, index: int) -> int:
        i = 0
        curr = self.head.next
        while curr:
            if index == i:
                return curr.val
            curr = curr.next
            i += 1
        return -1

    def insertHead(self, val: int) -> None:
        node = Node(val)
        node.next = self.head.next # since we're using a dummy node, set to head.next to set the real
        self.head.next = node
        if node.next is None:
            self.tail = node


    def insertTail(self, val: int) -> None:
        node = Node(val)
        self.tail.next = node
        self.tail = node


    def remove(self, index: int) -> bool:
        i = 0
        # we need the previous node, so lets get to
        # previous node relative to target (index)
        curr = self.head
        while curr and i < index:
            curr = curr.next
            i += 1

        # we're at the previous node
        if curr and curr.next:

            # handle the case where we're removing
            # the tail
            if curr.next == self.tail:
                self.tail = curr
            
            curr.next = curr.next.next
            return True

        return False


    def getValues(self) -> List[int]:
        arr = []
        curr = self.head.next # point to the first real node

        while curr:
            arr.append(curr.val)
            curr = curr.next

        return arr

        
