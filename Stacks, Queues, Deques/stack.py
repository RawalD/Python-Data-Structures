# Check if its empty
# Push a new item
# Pop an item
# Peek at the top item
# Return the size

class Stack(object):

    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def add_item(self, item):
        return self.items.append(item)

    def pop_item(self):
        return self.items.pop()

    def first_item(self):
        return self.items[self.size_of()-1]

    def size_of(self):
        return len(self.items)


new_stack = Stack()

print(new_stack.is_empty())
new_stack.add_item('Hey You!')
print(new_stack.pop_item())
new_stack.add_item('Hey Youuuuuu!')
new_stack.add_item('Hey All!')
print(new_stack.first_item())
print(new_stack.size_of())
