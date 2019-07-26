class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = 0
        self.storage = [None]*capacity

    def append(self, item):
        self.storage[self.current] = item
        self.current = (self.current + 1) % self.capacity

    def get(self):
        result = []

        def remove_none(i):
            if i is None:
                return False
            else:
                return True

        values = filter(remove_none, self.storage)

        for i in values:
            result.append(i)

        return result
