# Check if its empty
# Add to both front and rear
# Remove from Front and Rear
# Check the Size

class Deque(object):

    def __init__(self):
        self.items = []

    def empty_checK(self):
        return len(self.items) == 0

    def front_add(self, item):
        return self.items.insert(0, item)

    def back_add(self, item):
        return self.items.append(item)

    def front_remove(self):
        return self.items.pop(0)

    def back_remove(self):
        return self.items.pop()

    def length(self):
        return len(self.items)


deque = Deque()

print(deque.empty_checK())

deque.front_add("Rumi")
deque.front_add("Rumi_R")
deque.back_add("Dip")

print(deque.front_remove())
print(deque.back_remove())
print(deque.length())
