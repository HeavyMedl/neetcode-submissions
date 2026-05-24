class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity if capacity > 0 else 1
        self.array = [None] * self.capacity
        self.length = 0

    def get(self, i: int) -> int:
        if i < 0 or i > self.length:
            raise ValueError("i out of bounds")

        return self.array[i]

    def set(self, i: int, n: int) -> None:
        if i < 0 or i > self.length:
            raise ValueError("i out of bounds")

        self.array[i] = n

    def pushback(self, n: int) -> None:
        # if we're pushing, we need to check the capacity
        if self.length == self.capacity: # we are full, resize
            self.resize()
        
        self.array[self.length] = n
        self.length += 1


    def popback(self) -> int:
        if self.length > 0:
            self.length -= 1

        return self.array[self.length]

    def resize(self) -> None:
        newCapacity = 2 * self.capacity
        newArray = [None] * newCapacity

        # copy values over from previous array
        for i in range(self.length):
            newArray[i] = self.array[i]
        
        self.array = newArray
        self.capacity = newCapacity

    def getSize(self) -> int:
        return self.length
    
    def getCapacity(self) -> int:
        return self.capacity
