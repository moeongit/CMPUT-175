class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            raise Exception("Cannot pop from an empty stack")
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            raise Exception("Cannot peek an empty stack")
        return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)
# create a stack instance
my_stack = Stack()

# check if stack is empty
assert my_stack.is_empty() == True

# add items to stack
my_stack.push(1)
my_stack.push(2)
my_stack.push(3)

# check size of stack
assert my_stack.size() == 3

# peek at the top item on the stack
assert my_stack.peek() == 3

# remove top item from stack
assert my_stack.pop() == 3

# check size of stack again
assert my_stack.size() == 2

# remove remaining items from stack
assert my_stack.pop() == 2
assert my_stack.pop() == 1

# check if stack is empty again
assert my_stack.is_empty() == True
