class MinHeap:
  def __init__(self):
    self.heap = [0]

  def push(self, val: int) -> None:
    self.heap.append(val)  # append to end of heap

    # now bubble that value up, comparing to parent
    i = len(self.heap) - 1
    parent = i // 2

    while i > 1 and self.heap[i] < self.heap[parent]:
      self.heap[i], self.heap[parent] = self.heap[parent], self.heap[i]
      i = parent
      parent = i // 2

  def bubble_down(self, i: int) -> None:
    child = i * 2 # left child
    while child < len(self.heap):
        if child + 1 < len(self.heap) and self.heap[child + 1] < self.heap[child]:
            child += 1 # right child
        
        if self.heap[child] >= self.heap[i]:
            return

        self.heap[i], self.heap[child] = self.heap[child], self.heap[i]
        i = child
        child = i * 2

  def pop(self) -> int:
    if len(self.heap) < 2:
        return -1
    if len(self.heap) == 2:
        return self.heap.pop()
    
    top = self.heap[1]
    self.heap[1] = self.heap.pop()
    self.bubble_down(1)
    return top

  def top(self) -> int:
    return self.heap[1] if len(self.heap) > 1 else -1

  def heapify(self, nums: List[int]) -> None:
    self.heap = [0] + nums

    for i in range(len(self.heap) // 2, 0, -1):
        self.bubble_down(i)
