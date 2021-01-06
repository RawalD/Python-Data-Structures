class Queues(object):

    def __init__(self):
        self.stack_one_in = []
        self.stack_two_out = []

    def enqueue(self, element):

        self.stack_one_in.append(element)

    def dequeue(self):

        if not self.stack_two_out:
            while self.stack_one_in:
                self.stack_two_out.append(self.stack_one_in.pop())
        return self.stack_two_out.pop()


queue = Queues()

for i in range(5):
    queue.enqueue(i)

for j in range(5):
    print(queue.dequeue())
