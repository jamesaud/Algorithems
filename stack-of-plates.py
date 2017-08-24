"""
Imagine a (literal) stack of plates. If the stack gets too high, it might topple. Therefore, in real life, we would 
likely start a new stack when the previous stack exceeds some threshold. Implement a data structure SetOfStacks that 
mimics this. SetOfStacks should be composed of several stacks, and should create a new stack once the previous one 
exceeds capacity. SetOfStacks.push() and SetOfStacks.pop() should behave identically to a single stack 
(that is, pop() should return the same values as it would if there were just a single stack).
"""




class StackOfPlates:
    # Push(): Pushes ele to the top stack
    # Pop():  Removes ele from top of stack
    # is_empty(): Says whether all stacks are empty
    # Peek():  Look at top element of stack

    def __init__(self, max_stack_elements):
        self.stacks = [[]]  # List of stacks, where the last element is the most recent stack
        self.top_stack = self.stacks[0]  # The current stack being added to
        self.max = max_stack_elements   # The max elements one stack can contain


    def push(self, elem):
        if len(self.top_stack) == self.max:
            self.add_new_stack()

        self.top_stack.append(elem)

    def peek(self):
        return self.top_stack[-1]

    def pop(self):
        if not self.top_stack:
            del self.stacks[-1]
            self.top_stack = self.stacks[-1]
        return self.top_stack.pop()

    def add_new_stack(self):
        self.stacks.append([])
        self.top_stack = self.stacks[-1]

    def pop_at(self, index):
        stack_index = (index - 1) // self.max
        elem_index_in_stack = index % self.max
        del self.stacks[stack_index][elem_index_in_stack]
        self.__shift_stacks(stack_index)

    # Provide the unbalanced stack index
    def __shift_stacks(self, stack_index):
        while stack_index < (len(self.stacks) - 1):
            stack = self.stacks[stack_index]
            next = self.stacks[stack_index + 1]
            stack.append(next.pop(0))
            if not next: del self.stacks[-1]
            stack_index += 1


m = StackOfPlates(3)
m.push(2)
m.push(3)
m.push(4)
m.push(4)
m.push(4)

print(m.stacks)

m.pop_at(4)

print(m.stacks)

m.push(5)
m.push(6)
m.push(7)

print(m.stacks)

m.pop_at(3)

print(m.stacks)

