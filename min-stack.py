import heapq

from collections import namedtuple

# Worse implementation
# O(n) to re-heapify on element pop(), plus O(2n) space complexity
class MinStack:

    def __init__(self):
        self.stack = []
        self.min_heap = []

    def pop(self):
        self.min_heap.remove(self.stack[-1])
        heapq.heapify(self.min_heap)
        return self.stack.pop()

    def peek(self):
        return self.stack[-1]

    def push(self, elem):
        self.stack.append(elem)
        heapq.heappush(self.min_heap, elem)

    def is_empty(self):
        return True if self.stack else False

    def get_min(self):
        return self.min_heap[0]


class NumPair:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class BetterMinStack:

    def __init__(self):
        self.stack = []
        self.smallest = float("inf")

    def pop(self):
        num_pair = self.stack.pop()
        if num_pair.value == self.smallest:
            self.smallest = num_pair.next
        return num_pair.value

    def peek(self):
        return self.stack[-1].value

    def push(self, elem):
        if elem <= self.smallest:
            self.stack.append(NumPair(elem, next=self.smallest))
            self.smallest = elem
        else:
            self.stack.append(NumPair(elem))

    def is_empty(self):
        return True if self.stack else False

    def get_min(self):
        return self.smallest if self.stack else None



m = BetterMinStack()
m.push(3)
m.push(2)
m.push(4)

print(m.get_min())

m.pop()
m.pop()

m.push(1)
print(m.get_min())

m.pop()
print(m.get_min())
