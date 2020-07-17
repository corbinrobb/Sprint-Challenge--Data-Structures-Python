class RingBuffer:
    def __init__(self, capacity):
        self.storage = []
        self.capacity = capacity
        self.oldest = 0

    def append(self, item):
        if len(self.storage) == self.capacity:
            self.storage[self.oldest] = item
            if self.oldest + 1 == self.capacity:
                self.oldest = 0
            else:
                self.oldest += 1
        else:
            self.storage.append(item)


    def get(self):
        return self.storage
