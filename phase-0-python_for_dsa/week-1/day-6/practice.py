import heapq

class MaxHeap:
    def __init__(self):
        # Initialize an empty list assigned to this specific object instance
        self.heap = []

    def push(self, val: int) -> None:
        # 1. Take the positive val, negate it, and push it to self.heap
        
        heapq.heappush(self.heap,-val)
        print(self.heap)

    def pop(self) -> int:
        # 2. Pop the element from self.heap and return its positive value
        rm=-heapq.heappop(self.heap)
        return rm
    def peek(self) -> int:
        # 3. Look at index 0 of self.heap and return its positive value
        first=-self.heap[0]
        return first

    def __len__(self) -> int:
        # 4. Return the length of self.heap
        return len(self.heap)

# How we want to use it out in the wild:
mx = MaxHeap()
mx.push(1)
mx.push(2)
mx.push(3)

print(mx.peek())  # Should print 3
print(mx.pop())   # Should pop and print 3
print(len(mx))    # Should print 2