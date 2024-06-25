class DynamicFIFO:
    def __init__(self):
        self.buffer = []

    def push(self, value):
        self.buffer.append(value)

    def pop(self):
        return self.buffer.pop(0)